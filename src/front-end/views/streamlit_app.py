import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Test Pilot",
        options=["Create Task", "Task List", "Settings"],
        icons=["plus-circle", "list-task", "gear"],
        menu_icon="bug",
        default_index=0,
    )

with st.sidebar:
    st.markdown("---")
    st.write("Version:", "1.0.0")
    st.write("©️ 2024 Global Analyst Challenge")


if selected == "Create Task":
    st.subheader(f"**You Have selected {selected}**")

if selected == "Task List":
    st.subheader(f"**You Have selected {selected}**")

if selected == "Settings":
    st.subheader(f"**You Have selected {selected}**")



