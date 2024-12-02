import streamlit as st
import requests
from typing import List, Dict, Optional


# Mock 数据和 API 数据获取逻辑
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


# Mock data for local testing
mock_data = [
    {
        "id": "674aaf22c2978c23ab85e541",
        "task_name": "task1",
        "description": "test",
        "prompt": "",
        "parameters": "test",
        "status": "running",
        "test_plan": "",
        "test_script": "",
        "url": "http://www.baidu.com",
        "html_code": "",
        "created_time": ""
    },
    {
        "id": "674bfa19f8c9847521e3a77f",
        "task_name": "task2",
        "description": "test",
        "prompt": "",
        "parameters": "test",
        "status": "success",
        "test_script": "",
        "url": "http://www.baidu.com",
        "html_code": "",
        "created_time": ""
    },
    {
        "id": "674bfa19f8c9847521e3a70f",
        "task_name": "task3",
        "description": "test",
        "prompt": "",
        "parameters": "test",
        "status": "failed",
        "test_plan": "",
        "test_script": "",
        "url": "http://www.baidu.com",
        "html_code": "",
        "created_time": ""
    }
]

# Replace with actual API fetching if needed
all_tasks = mock_data  # Replace with fetch_tasks()


class TaskLists:
    """
    TaskLists class handles displaying and interacting with task lists and details.
    """

    def __init__(self):
        # Initialize session state variables
        st.session_state.setdefault("view", "list")
        st.session_state.setdefault("current_task", None)

    def view(self):
        """
        Render the main view based on the current session state.
        """
        content = st.container()

        if st.session_state["view"] == "list":
            with content:
                self.display_task_list_view()
        else:
            with content:
                task = st.session_state["current_task"]
                if task:
                    self.display_task_detail_view(task)
                else:
                    st.error("No task selected.")

    def display_task_list_view(self):
        """
        Display the task list view with tabs for all tasks, running tasks, and completed tasks.
        """
        st.title("Task List")
        tabs = st.tabs(["All Tasks", "Running Tasks", "Completed Tasks"])

        # Filter tasks by status
        running_tasks = [t for t in all_tasks if t["status"] == "running"]
        completed_tasks = [t for t in all_tasks if t["status"] != "running"]

        # Display task lists under tabs
        with tabs[0]:
            self.display_task_list(all_tasks, "all-tasks")
        with tabs[1]:
            self.display_task_list(running_tasks, "running-tasks")
        with tabs[2]:
            self.display_task_list(completed_tasks, "completed-tasks")

    def display_task_list(self, tasks: List[Dict], prefix: str):
        """
        Display a list of tasks with details and actions.

        :param tasks: List of tasks to display.
        :param prefix: Unique prefix for button keys to avoid conflicts.
        """
        for task in tasks:
            cols = st.columns([3, 4, 2, 1])  # Layout for task details
            cols[0].write(task["task_name"])  # Task name
            cols[1].write(task["url"])  # Task URL
            cols[2].write(task["status"])  # Task status
            if cols[3].button("Details", key=f"{prefix}-view-{task['id']}"):
                # Set the current task and switch to detail view
                st.session_state["current_task"] = task
                st.session_state["view"] = "detail"
                st.rerun()

    def display_task_detail_view(self, task: Dict):
        """
        Display the task detail view with tabs for different sections.

        :param task: Task details to display.
        """
        if st.button("Back"):
            st.session_state["view"] = "list"
            st.session_state["current_task"] = None
            st.rerun()

        tabs = st.tabs(["Main", "HTML Code", "Test Plan", "Test Script"])
        with tabs[0]:
            self.display_task_main_info(task)
        with tabs[1]:
            self.display_html_code()
        with tabs[2]:
            self.display_test_plan()
        with tabs[3]:
            self.display_test_script()

    def display_task_main_info(self, task: Dict):
        """
        Display the main information of a task.

        :param task: Task details to display.
        """
        st.header(f"Task: {task['task_name']}")
        st.write(f"URL: {task['url']}")
        st.write(f"Status: {task['status']}")

    def display_html_code(self):
        """Placeholder for displaying HTML code."""
        st.write("HTML Code Content")

    def display_test_plan(self):
        """Placeholder for displaying the test plan."""
        st.write("Test Plan Content")

    def display_test_script(self):
        """Placeholder for displaying the test script."""
        st.write("Test Script Content")