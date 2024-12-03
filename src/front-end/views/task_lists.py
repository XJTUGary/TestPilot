# coding=utf-8
import streamlit as st
import requests


@st.cache_data
def fetch_tasks():
    url = "/api/vi/management/task-list"  # 替换为实际的 API 地址
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch tasks: {e}")
        return []


mock_data = [
    {
        "id": "674aaf22c2978c23ab85e541",
        "task_name": "task1",
        "description": "test",
        "prompt": "",
        "parameter": "test",
        "status": "running",
        "test_plan": """{
"test":[
{
"id":"1",
"module_title":"Search Input Functionality"
}
]
}""",
        "test_script": """import rc
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto('https://www.baidu.com')
    print(page.title())

    browser.close()""",
        "url": "http://www.baidu.com",
        "http_code": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>简单的 HTML 页面</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
    }
    h1 {
        color: #333;
    }
</style>
</head>
<body>
<h1>Hello, World!</h1>
<p>这是一个简单的 HTML 页面示例。</p>
</body>
</html>"""
    },
    {
        "id": "674bfa19f8c9847521e3a77f",
        "task_name": "task2",
        "description": "test",
        "prompt": "",
        "parameter": "test",
        "status": "success",
        "test_plan": "",
        "test_script": "",
        "url": "http://www.baidu.com",
        "http_code": ""
    },
    {
        "id": "674bfa19f8c9847521e3a70f",
        "task_name": "task3",
        "description": "test",
        "prompt": "",
        "parameter": "test",
        "status": "failed",
        "test_plan": "",
        "test_script": "",
        "url": "http://www.baidu.com",
        "http_code": ""
    },
]

all_tasks = mock_data  # fetch_tasks()


# 显示任务列表
def display_task_list(tasks, prefix):
    with st.container(border=True):
        header_cols = st.columns([3, 4, 2, 1])
        header_cols[0].write("__Task Name__")
        header_cols[1].write("__Test URL__")
        header_cols[2].write("__Status__")
        header_cols[3].write("__Action__")
    for task in tasks:
        cols = st.columns([3, 4, 2, 1])  # 分列显示
        cols[0].write(task["task_name"])  # 第一列：任务名
        cols[1].write(task["url"])  # 第二列：URL
        cols[2].write(task["status"])  # 第三列：状态
        # 第四列：按钮
        if cols[3].button("view", key=f"{prefix}-view-{task['id']}"):
            # 设置当前任务并切换到详情页
            st.session_state["current_task"] = task
            st.session_state["view"] = "detail"
            st.rerun()
        st.divider()


# 显示任务详情
def display_task_detail(task):
    # 创建两列布局
    button_col, expander_col = st.columns([1, 5])
    with button_col:
        back_btn = st.button("Back")

    with expander_col:
        with st.expander("Task Info"):
            st.write("__Description:__ " + task["description"])
            st.write("__Prompt:__ " + task["prompt"])
            st.write("__Parameter:__ " + task["parameter"])
            st.write("__Status:__ " + task["status"])
    if back_btn:
        st.session_state["view"] = "list"
        st.session_state["current_task"] = None
        st.rerun()

    # 渲染任务详情的标签页
    tab_main, tab_html_code, tab_step, tab_script = st.tabs(
        ["Main", "HTML Code", "Test Step", "Test Script"]
    )

    with tab_main:
        st.header(f"Task: {task['task_name']}")
        st.write(f"URL: {task['url']}")
        st.write(f"Status: {task['status']}")
    with tab_html_code:
        code = task["http_code"]
        st.code(code, language='cshtml')
    with tab_step:
        code = task["test_plan"]
        st.code(code, language='json')
    with tab_script:
        code = task["test_script"]
        st.code(code, language='python')


# 初始化 session_state
if "view" not in st.session_state:
    st.session_state["view"] = "list"
if "current_task" not in st.session_state:
    st.session_state["current_task"] = None

# 动态内容容器
content = st.container()

# 根据当前视图显示内容
if st.session_state["view"] == "list":
    with content:
        st.title("Task List")
        tabs = st.tabs(["All Tasks", "Running Tasks", "Completed Tasks"])

        running_tasks = [t for t in all_tasks if t["status"] == "running"]
        completed_tasks = [t for t in all_tasks if t["status"] != "running"]

        with tabs[0]:  # All Tasks
            display_task_list(all_tasks, "all-tasks")
        with tabs[1]:  # Running Tasks
            display_task_list(running_tasks, "running-tasks")
        with tabs[2]:  # Completed Tasks
            display_task_list(completed_tasks, "completed-tasks")
else:
    with content:
        task = st.session_state["current_task"]
        if task:
            display_task_detail(task)
        else:
            st.error("No task selected.")

st.markdown(
    """
    <style>
    .stButton > button {
        color: white;
        background-color: #5cb85c;
        width: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
