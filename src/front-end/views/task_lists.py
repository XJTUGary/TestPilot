import streamlit as st
import requests
from typing import List, Dict


@st.cache_data
def fetch_tasks() -> List[Dict]:
    """
    Fetch tasks from the backend API.
    Returns a list of task dictionaries.
    """
    url = "/api/v1/management/task-list"  # Replace with the actual API URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch tasks: {e}")
        return []


def get_test_cases_by_taskid(task_id):
    url = "http://127.0.0.1:5000/api/case-list"
    params = {'task_id': task_id}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch tasks: {e}")
        return []


# Mock data for local testing
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


class TaskLists:
    """
    TaskLists class handles displaying and interacting with task lists and details.
    """

    def __init__(self):
        st.session_state.setdefault("view", "list")
        st.session_state.setdefault("current_task", None)
        st.session_state.setdefault("current_script", " ")

    def view(self):
        """
        Render the main view based on the current session state.
        """
        if st.session_state["view"] == "list":
            self.display_task_list_view()
        else:
            task = st.session_state["current_task"]
            if task:
                self.display_task_detail_view(task)
            else:
                st.error("No task selected.")

    def display_task_list_view(self):
        """
        Display the task list view with tabs for all tasks, running tasks, and completed tasks.
        """
        st.title("📝 Task Management Dashboard")

        tabs = st.tabs(["📋 All Tasks", "⚙️ Running Tasks", "✅ Completed Tasks"])

        # Filter tasks
        running_tasks = [t for t in all_tasks if t["status"] == "running"]
        completed_tasks = [t for t in all_tasks if t["status"] != "running"]

        # Display tasks in each tab
        with tabs[0]:
            self.render_task_table("All", all_tasks)
        with tabs[1]:
            self.render_task_table("Running", running_tasks)
        with tabs[2]:
            self.render_task_table("Completed", completed_tasks)

    def render_task_table(self, status: str, tasks: List[Dict]):
        """
        Display tasks in a table layout with action buttons.
        """
        if not tasks:
            st.info("No tasks available.")
            return

        for task in tasks:
            with st.form(key=f"task-{status}-{task['id']}"):
                cols = st.columns([3, 4, 2, 2])  # Layout for task details
                cols[0].markdown(f"**Task Name**: {task['task_name']}")
                cols[1].markdown(f"**URL**: [{task['url']}]({task['url']})")
                cols[2].markdown(f"**Status**: `{task['status']}`")
                cols[3].form_submit_button("View", on_click=self.select_task, args=(task,), type="primary")

            st.divider()

    def select_task(self, task: Dict):
        """
        Set the selected task and switch to detail view.
        """
        st.session_state["current_task"] = task
        st.session_state["view"] = "detail"
        st.rerun()

    def display_task_detail_view(self, task: Dict):
        """
        Display task details with tabs for additional information.
        """
        st.title(f"📄 Task Details - {task['task_name']}")

        if st.button("🔙 Back to Task List"):
            st.session_state["view"] = "list"
            st.session_state["current_task"] = None
            st.rerun()

        # Tabs for different sections
        tabs = st.tabs(["🔍 Overview", "💻 HTML Code", "📝 Test Plan", "📜 Test Script"])
        case_list = get_test_cases_by_taskid(task['id'])

        with tabs[0]:
            st.subheader("General Information")
            st.write(f"- **Task Name**: {task['task_name']}")
            st.write(f"- **URL**: [{task['url']}]({task['url']})")
            st.write(f"- **Status**: `{task['status']}`")
            st.write(f"- **Description**: {task['description']}")

        with tabs[1]:
            code = task["http_code"]
            st.code(code, language='cshtml')

        with tabs[2]:
            code = case_list
            st.json(code)

        with tabs[3]:
            code_col, case_lists_col = st.columns([5, 2])
            with code_col:
                st.code(st.session_state["current_script"], language='python')
            with case_lists_col:
                for case in case_list:
                    with st.container(border=True):
                        cols = st.columns(2)
                        cols[0].write(case["test_name"])
                        cols[1].button("script", key=f"{case['test_name']}", type="primary",
                                       on_click=self.script_btn, args=(f"{case['script']}",))

    def script_btn(self, script=None):
        print(script)
        if script is not None:
            st.session_state["current_script"] = script
        else:
            st.session_state["current_script"] = ""

