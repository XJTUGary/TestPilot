# coding=utf-8
import requests
import streamlit as st


def get_html_code():
    # # 发送POST请求
    # try:
    #     url = "localhost:8080/htmlcode"
    #     # 准备数据
    #     get_params = {'task_name': "required_task_name",
    #                   'task_id': "required_task_id",
    #                   }
    #     response = requests.post(url, data=get_params)
    #     response.raise_for_status()  # 检查是否有HTTP错误
    #     # 显示结果
    #     return response.json()
    # except requests.exceptions.RequestException as e:
    #     st.error(f"错误: {e}")

    with open("../mock/htmlcode.txt", 'r') as file:
        return file.read()


def get_test_step():
    # # 发送POST请求
    # try:
    #     url = "localhost:8080/testplan"
    #     # 准备数据
    #     get_params = {'task_name': "required_task_name",
    #                   'task_id': "required_task_id",
    #                   }
    #     response = requests.post(url, data=get_params)
    #     response.raise_for_status()  # 检查是否有HTTP错误
    #     # 显示结果
    #     return response.json()
    # except requests.exceptions.RequestException as e:
    #     st.error(f"错误: {e}")

    with open("../mock/testplan.txt", 'r') as file:
        return file.read()


def get_test_script():
    # # 发送POST请求
    # try:
    #     url = "localhost:8080/testscript"
    #     # 准备数据
    #     get_params = {'task_name': "required_task_name",
    #                   'task_id': "required_task_id",
    #                   }
    #     response = requests.post(url, data=get_params)
    #     response.raise_for_status()  # 检查是否有HTTP错误
    #     # 显示结果
    #     return response.json()
    # except requests.exceptions.RequestException as e:
    #     st.error(f"错误: {e}")

    with open("../mock/testscript.txt", 'r') as file:
        return file.read()


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
