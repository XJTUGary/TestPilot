import streamlit as st


class CreateTask:
    def view(self):
        with st.form(key='task_form'):
            st.header("Base Content")

            # Task name (required)
            task_name = st.text_input("Task Name *", help="Enter the name of the task")
            description = st.text_area("Description", help="Provide a description for the task")
            url = st.text_input("URL *", help="Enter the URL related to the task")

            st.header("User Story")

            # Custom prompt (required)
            custom_prompt = st.text_area("Custom Prompt", help="Provide a custom prompt for the task")

            # Parameters (optional)
            parameters = st.text_area("Parameters", help="Provide any parameters for the task (e.g., key=value pairs)")

            # Submit button inside form
            submit_button = st.form_submit_button("Create Task")