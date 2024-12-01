# coding=utf-8
import streamlit as st

tab_all, tab_running, tab_completed = st.tabs(
    ["All Tasks", "Running Tasks", "Completed Tasks"])

with tab_all:
    st.header("All Tasks")

    st.page_link("test_case_detail.py",
                 label="redirect to test case detail",
                 icon="🔥")

with tab_running:
    st.header("Running Tasks")


with tab_completed:
    st.header("Completed Tasks")

