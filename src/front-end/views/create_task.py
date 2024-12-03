import streamlit as st
import time

with st.form(key='task_form', clear_on_submit=True, border=False):
    # Base Content in an expander
    with st.expander("Base Content", expanded=True):
        # Task name (required)
        task_name = st.text_input("Task Name *", help="Enter the name of the task")
        description = st.text_area("Description", help="Provide a description for the task")
        url = st.text_input("URL *", help="Enter the URL related to the task")

    # User Story in an expander
    with st.expander("User Story"):
        # Custom prompt (required)
        custom_prompt = st.text_area("Custom Prompt", help="Provide a custom prompt for the task")

        # Parameters (optional)
        parameters = st.text_area("Parameters", height=136,
                                  placeholder="{\n\t\"username\": \"Gary\"\n\t\"password\": \"pwd\"\n}",
                                  help="Provide any parameters for the task (e.g., key=value pairs)")

    # Submit button inside form
    submit_button = st.form_submit_button("Create Task", type="primary")
    # Create an empty placeholder for success/error message
    status_placeholder = st.empty()

if submit_button:
    if task_name and url:
        # Show success message
        status_placeholder.success("Task Created Successfully!")

        # Wait for 2 seconds before clearing the message
        time.sleep(1.5)
        status_placeholder.empty()  # Clear the message after a delay
    else:
        # Show error message
        status_placeholder.error("Please fill in all required fields (Task Name, URL).")

        # Wait for 2 seconds before clearing the message
        time.sleep(1.5)
        status_placeholder.empty()  # Clear the message after a delay
