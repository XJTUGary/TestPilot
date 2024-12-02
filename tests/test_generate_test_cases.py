import unittest
from generate_test_cases import GenerateTestCases


class TestGenerateTestCases(unittest.TestCase):
    def test_html2cases(self):
        """

        """
        # 初始化 GenerateScript 实例
        generate_test_cases  = GenerateTestCases()

        # 输入 url, user_prompt
        # url = "https://www.baidu.com"
        url = "https://www.youtube.com"
        user_prompt = ""

        # 调用
        result = generate_test_cases.generateTestCases(url, user_prompt)

        # 打印结果
        print("Test Cases:")
        print(result)


if __name__ == "__main__":
    unittest.main()
