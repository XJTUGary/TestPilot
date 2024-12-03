# coding=utf-8
import requests
import streamlit as st

baseUrl = "https://back-end-url/api/vi/management"
mockdata = {
    "description": "here is the user description for test task",
    "prompt": "here is the user prompt for test task",
    "params": "here is the user params for test task",
    "status": "here is the user status for test task",
}


def get_task_detail():
    # 发送POST请求
    try:
        url = baseUrl + "/task"
        "localhost:8080/htmlcode"
        # 准备数据
        get_params = {'task_id': "required_task_id"}
        response = requests.post(url, data=get_params)
        response.raise_for_status()  # 检查是否有HTTP错误
        # 显示结果
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"错误: {e}")


def get_html_code():
    # return get_task_detail().http_code

    with open("../mock/htmlcode.txt", 'r') as file:
        return file.read()


def get_test_step():
    # return get_task_detail().test_plan

    with open("../mock/testplan.txt", 'r') as file:
        return file.read()


def get_test_script():
    # return get_task_detail().test_script

    with open("../mock/testscript.txt", 'r') as file:
        return file.read()


st.subheader(":green[<] task name")

with st.expander("task info"):
    st.write(mockdata["description"])
    st.write(mockdata["prompt"])
    st.write(mockdata["params"])
    st.write(mockdata["status"])

tab_main, tab_html_code, tab_step, tab_script = st.tabs(
    ["__Main__", "__HTML Code__", "__Test Plan__", "__Test Script__"])

with tab_main:
    st.header("main tab")

with tab_html_code:
    code = get_html_code()
    st.code(code, language='cshtml')

with tab_step:
    code = get_test_step()
    st.code(code, language='json')

with tab_script:
    code = get_test_script()
    st.code(code, language='python')
