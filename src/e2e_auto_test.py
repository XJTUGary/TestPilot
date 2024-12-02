from llms.llm_provider import LLMProvider
from generate_test_cases import GenerateTestCases
from generate_test_step import GenerateTestStep
from generate_script import GenerateScript


class E2EAutoTest:
    def __init__(self):
        self.llm_provider = LLMProvider()
        self.generate_test_cases = GenerateTestCases(self.llm_provider)
        self.generate_test_step = GenerateTestStep(self.llm_provider)
        self.generate_script = GenerateScript(self.llm_provider)

    def run_test(self, url, user_prompt=None, parameters=None):
        test_cases, web_content = self.generate_test_cases.generateTestCases(url, user_prompt)

        for test_case in test_cases["test_cases"]:
            test_step = self.generate_test_step.case2step(
                test_description=test_case["test_description"],
                url=url,
                web_content=web_content
            )
            test_script = self.generate_script.step2code(test_step)
            print(test_script)


if __name__ == "__main__":
    e2e = E2EAutoTest()
    e2e.run_test("https://www.baidu.com")