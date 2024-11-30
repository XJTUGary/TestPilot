import streamlit as st
import asyncio
import websockets
import json
from PIL import Image
import base64
import io

st.set_page_config(layout="wide", page_title="Playwright TestPilot")

# 页面标题
st.title("🔍 Playwright TestPilot - Real-time Execution")

# 布局：左侧内嵌浏览器，右侧测试用例
col1, col2 = st.columns([2, 1])

# 左侧实时浏览器截图展示
with col1:
    st.markdown("### Browser Execution")
    browser_placeholder = st.empty()  # 动态更新截图占位符

# WebSocket 客户端连接
async def send_test_case(test_case):
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"test_case": test_case}))

            while True:
                message = await websocket.recv()
                data = json.loads(message)
                print(data)  # 控制台打印日志

                # 更新日志
                if data["status"] == "Test completed":
                    st.session_state["log"].append("Execution completed")
                    break
                elif data.get("screenshot"):
                    screenshot_data = base64.b64decode(data["screenshot"])
                    image = Image.open(io.BytesIO(screenshot_data))
                    browser_placeholder.image(image, caption="Live View", use_container_width=True)

                st.session_state["log"].append(data["status"])

                # 避免过快刷新导致卡顿
                await asyncio.sleep(0.1)
    except Exception as e:
        st.session_state["log"].append(f"Error: {str(e)}")

# 初始化会话状态
if "log" not in st.session_state:
    st.session_state["log"] = []

# 右侧测试用例
with col2:
    st.markdown("### Test Cases")
    test_cases = {
        "Search on Baidu": """print("Navigating to Baidu homepage...")\nawait page.goto("https://www.baidu.com/")\nawait page.locator("#kw").fill("hackathon")\nawait page.locator("#su").click()""",
        "Visit Example": """await page.goto("https://example.com")\nawait page.wait_for_load_state("networkidle")""",
    }

    for name, code in test_cases.items():
        if st.button(name):
            asyncio.run(send_test_case(code))

    st.markdown("### Logs")
    st.write("\n".join(st.session_state["log"][-10:]))  # 显示最新 10 条日志