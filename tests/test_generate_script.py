import unittest
from generate_script import GenerateScript
from utils.utils import Utils


class TestGenerateScript(unittest.TestCase):
    def test_step2code(self):
        """
        Test the step2code method with a simple input.
        """
        # 初始化 GenerateScript 实例
        generate_script = GenerateScript()

        # 输入 plan_text
        plan_text = '''
            1.	Setup Environment:
            •	Install Playwright: pip install playwright.
            •	Install necessary browsers: playwright install.
            2.	Import Dependencies:
            •	Import Playwright in Python: from playwright.sync_api import sync_playwright.
            3.	Define Test Scope:
            •	Create a test script file, e.g., test_search.py.
            •	Include necessary test framework setups, like pytest if needed.
            4.	Launch Browser:
            •	Use Playwright to launch the browser (chromium, firefox, or webkit).
            •	Configure browser launch options (headless or non-headless).
            5.	Navigate to URL:
            •	Open the specified URL: https://www.baidu.com/.
            6.	Locate Elements:
            •	Identify the search box (#kw) and search button (#su).
            7.	Simulate User Input:
            •	Type a query into the search box: page.fill("#kw", "Playwright testing").
            8.	Trigger Search:
            •	Click the search button: page.click("#su").
            9.	Verify Search Action:
            •	Wait for the search results page to load.
            •	Verify the URL change or search results’ presence.
            •	Example: assert "Playwright testing" in page.url.
            10.	Close Browser:
            •	Close the browser instance to clean up.
            11.	Run Test:
            •	Execute the script using pytest or directly with Python.
            12.	Document Results:
            •	Log outputs and results of the test.
        '''

        # 调用 step2code 方法
        result = generate_script.step2code(plan_text)

        # 打印结果
        print("Generated Playwright Code:")
        print(result)


if __name__ == "__main__":
    unittest.main()
