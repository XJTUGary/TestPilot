# coding=utf-8
import streamlit as st

tab_main, tab_html_code, tab_step, tab_script = st.tabs(
    ["Main", "HTML Code", "Test Plan", "Test Script"])

with tab_main:
    st.header("main tab")

with tab_html_code:
    st.header("html code")

with tab_step:
    st.header("test step ")


with tab_script:
    st.header("test script")

