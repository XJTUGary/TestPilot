from generate_script import GenerateScript
from generate_test_cases import GenerateTestCases
from generate_test_step import GenerateTestStep
from llms.llm_provider import LLMProvider
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import requests


app = FastAPI()
task_id = None

headers = {"Content-Type": "application/json"}
create_cases_url = ""


class TaskRequest(BaseModel):
    task_id: str
    url: str
    user_prompt: Optional[str] = None  # user_prompt 为可选参数
    parameters: Optional[dict] = None  # parameters 为可选参数


@app.post("/run_task/")
async def run_task(request: TaskRequest):
    global task_id
    task_id = request.task_id
    url = request.url
    user_prompt = request.user_prompt
    parameters = request.parameters

    e2e = E2EAutoTest()
    e2e.run_test(url=url, user_prompt=user_prompt, parameters=parameters)
    return None


class E2EAutoTest:
    def __init__(self):
        self.llm_provider = LLMProvider()
        self.generate_test_cases = GenerateTestCases(self.llm_provider)
        self.generate_test_step = GenerateTestStep(self.llm_provider)
        self.generate_script = GenerateScript(self.llm_provider)

    def run_test(self, url, user_prompt=None, parameters=None):
        test_cases, web_content = self.generate_test_cases.generateTestCases(url, user_prompt)

        # create cases 调用后端服务
        # self.save_cases(test_cases)
        for test_case in test_cases["test_cases"]:
            test_step = self.generate_test_step.case2step(
                test_description=test_case["test_description"],
                url=url,
                web_content=web_content
            )
            test_script = self.generate_script.step2code(test_step)

            # update case, add test script

            print(test_script)

    def save_cases(self, test_cases):
        global task_id

        data = {
            "task_id": task_id,
            "cases": test_cases["test_cases"]
        }

        response = requests.post(create_cases_url, json=data, headers=headers)

        if response.status_code == 200:
            print("请求成功！")
            return response.json()
        else:
            print(f"请求失败, 状态码: {response.status_code}")
            return None






if __name__ == "__main__":
    e2e = E2EAutoTest()
    e2e.run_test("https://www.baidu.com")
