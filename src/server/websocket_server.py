import asyncio
import textwrap
import websockets
import json
import base64
from playwright.async_api import async_playwright

async def websocket_handler(websocket):
    print("Client connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            test_case_code = data.get("test_case")
            if not test_case_code:
                await websocket.send(json.dumps({"status": "No test case received"}))
                continue

            try:
                # 使用 async_playwright
                async with async_playwright() as playwright:
                    browser = await playwright.chromium.launch(headless=True)  # 无头模式
                    context = await browser.new_context()
                    page = await context.new_page()

                    # 使用 exec 动态执行测试代码
                    exec_globals = {"page": page, "playwright": playwright, "asyncio": asyncio}
                    exec(f"async def run_test():\n{textwrap.indent(test_case_code, '    ')}", exec_globals)

                    # 开启测试任务
                    test_task = asyncio.create_task(exec_globals["run_test"]())

                    # 截图任务：每隔0.05秒截一次
                    screenshot_index = 0
                    while not test_task.done():  # 如果测试任务未完成
                        screenshot = await page.screenshot()

                        # 发送截图
                        screenshot_base64 = base64.b64encode(screenshot).decode("utf-8")
                        await websocket.send(json.dumps({
                            "status": "running",
                            "screenshot": screenshot_base64
                        }))
                        await asyncio.sleep(0.005)  # 每隔 0.5 秒截一次

                    # 等待测试任务完成
                    await test_task

                    # 完成后发送完成状态
                    await websocket.send(json.dumps({"status": "Test completed"}))

                    await context.close()
                    await browser.close()

            except Exception as e:
                await websocket.send(json.dumps({"status": f"Error: {str(e)}"}))

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(websocket_handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())