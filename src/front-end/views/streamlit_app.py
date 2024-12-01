import streamlit as st
from streamlit_option_menu import option_menu
from create_task import CreateTask

pg = st.navigation(
    [st.Page("create_task.py"),
     st.Page("task_lists.py"),
     st.Page("test_case_detail.py"),
     st.Page("settings.py")], position="hidden")
pg.run()

with st.sidebar:
    st.header("Test Pilot")
    st.page_link("create_task.py", label="Create Task")
    st.page_link("task_lists.py", label="Task List")
    st.page_link("settings.py", label="Settings")
    # selected = option_menu(
    #     menu_title="Test Pilot",
    #     options=["Create Task", "Task List", "Settings"],
    #     icons=["plus-circle", "list-task", "gear"],
    #     menu_icon="bug",
    #     default_index=0,
    # )

with st.sidebar:
    st.markdown("---")
    st.write("Version:", "1.0.0")
    st.write("©️ 2024 Global Analyst Challenge")

# if selected == "Create Task":
#     CreateTask().view()
#
# if selected == "Task List":
#     TaskLists().view()
#     # st.subheader(f"**You Have selected {selected}**")
#
# if selected == "Settings":
#     st.subheader(f"**You Have selected {selected}**")


