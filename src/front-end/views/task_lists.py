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


# Mock data for local testing
mock_data = [
    {"id": "674aaf22c2978c23ab85e541", "task_name": "Task 1", "status": "running", "url": "http://example.com", "description": "Test description"},
    {"id": "674bfa19f8c9847521e3a77f", "task_name": "Task 2", "status": "success", "url": "http://example.com", "description": "Another test"},
    {"id": "674bfa19f8c9847521e3a70f", "task_name": "Task 3", "status": "failed", "url": "http://example.com", "description": "Failure case"},
]

all_tasks = mock_data


class TaskLists:
    """
    TaskLists class handles displaying and interacting with task lists and details.
    """

    def __init__(self):
        st.session_state.setdefault("view", "list")
        st.session_state.setdefault("current_task", None)

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
                cols[3].form_submit_button("Details", on_click=self.select_task, args=(task,))

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

        with tabs[0]:
            st.subheader("General Information")
            st.write(f"- **Task Name**: {task['task_name']}")
            st.write(f"- **URL**: [{task['url']}]({task['url']})")
            st.write(f"- **Status**: `{task['status']}`")
            st.write(f"- **Description**: {task['description']}")

        with tabs[1]:
            st.subheader("HTML Code")
            st.text_area("HTML Code", "Placeholder for HTML code...", height=200)

        with tabs[2]:
            st.subheader("Test Plan")
            st.text_area("Test Plan", "Placeholder for test plan...", height=200)

        with tabs[3]:
            st.subheader("Test Script")
            st.text_area("Test Script", "Placeholder for test script...", height=200)
