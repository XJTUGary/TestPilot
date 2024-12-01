import unittest
from generate_script import GenerateScript


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

        plan_text2 = '''
        ## Step-by-Step Plan to Write Playwright Test for "Click Me Green" Button\n\nThis plan outlines the creation 
        of a Playwright test in Python to verify the functionality of the "Click Me Green" button on the provided 
        HTML.  We will use the Page Object Model (POM) for better organization and maintainability.\n\n**Phase 1: 
        Project Setup and POM Structure**\n\n1. **Create Project Directory:** Create a new directory for your 
        Playwright project (e.g., `playwright_test`).\n\n2. **Install Playwright:**  Use pip to install Playwright: 
        `pip install playwright`\n\n3. **Install Playwright Browsers:** Install the browsers you want to test with: 
        `playwright install`\n\n4. **Create POM Files:** Create Python files to represent the page structure.  For 
        this simple example, one file might suffice:\n\n   * `demo_page.py`: This will contain the Page Object class 
        for interacting with the demo page.\n\n**Phase 2:  `demo_page.py` (Page Object Model)**\n\nThis file will 
        define a class to encapsulate interactions with the demo page.\n\n```python\nfrom playwright.sync_api import 
        Page\n\nclass DemoPage:\n    def __init__(self, page: Page):\n        self.page = page\n        self.button = 
        page.locator("button:has-text(\'Click Me (Green)\')")  #Locator for the button\n        self.green_text = 
        page.locator("#pText") #Locator for the text element that changes color\n        self.readonly_text = 
        page.locator("#readOnlyText") #Locator for the readonly text element\n\n\n    def click_green_button(self):\n 
               self.button.click()\n\n    def get_green_text(self):\n        return self.green_text.inner_text()\n\n  
                 def get_readonly_text(self):\n        return self.readonly_text.inner_text()\n\n```\n\n**Phase 3: 
                 Test Script (`test_button.py`)**\n\nThis file will contain the actual Playwright test using the 
                 `DemoPage` class.\n\n```python\nimport pytest\nfrom playwright.sync_api import sync_playwright\nfrom 
                 demo_page import DemoPage\n\ndef test_click_green_button(page):\n    #This is a fixture provided by 
                 Playwright, it launches the browser and provides a page object\n\n    demo_page = DemoPage(page)\n   
                  initial_text = demo_page.get_green_text()\n    initial_readonly_text = demo_page.get_readonly_text(
                  )\n\n    demo_page.click_green_button()\n\n    #Assertions using expect to check if the text 
                  changed color after the button click\n    page.expect_inner_text(demo_page.green_text, "This Text 
                  is Purple")\n    page.expect_inner_text(demo_page.readonly_text, "The Color is Purple")\n\n    
                  #Clean up - change back to green.  This is optional but good practice for leaving the page in a 
                  known state\n    demo_page.click_green_button()\n    page.expect_inner_text(demo_page.green_text, 
                  initial_text)\n    page.expect_inner_text(demo_page.readonly_text, 
                  initial_readonly_text)\n\n```\n\n**Phase 4: Running the Test**\n\n1.  **Navigate to the page:**  
                  The `page` fixture in the test automatically handles navigation to the URL (you would specify the 
                  URL in your `pytest.ini` or similar configuration file if you were running multiple tests against 
                  different pages).\n\n2.  **Run pytest:** Execute the test using `pytest`.  Playwright will 
                  automatically handle browser launching and test execution.\n\n\n**Phase 5:  CI/CD 
                  Integration**\n\n1.  **Configuration:** Configure your CI/CD pipeline (e.g., GitHub Actions, 
                  GitLab CI, Jenkins) to run `pytest` within a suitable environment.\n\n2.  **Reporting:** Integrate 
                  a reporting tool (e.g., Allure, pytest-html) to generate comprehensive test reports for your CI/CD 
                  pipeline.\n\n3.  **Parallel Execution:** Playwright supports parallel test execution. Configure 
                  your CI/CD pipeline to run tests in parallel to reduce execution time.\n\n\n**Important 
                  Considerations:**\n\n*   **Error Handling:**  The provided code uses `expect` which provides 
                  implicit waiting and error handling.  If you need more explicit error handling, you can use 
                  try-except blocks.\n*   **Wait Strategies:** Playwright\'s auto-waiting is generally sufficient for 
                  this example.  For more complex scenarios, use explicit waits (`page.wait_for_selector`, 
                  etc.) if needed.\n*   **Screenshots/Videos:** Playwright allows capturing screenshots and videos on 
                  failure. Add this to your test if needed for debugging.\n*   **Input Validation:**  This test 
                  implicitly validates the button\'s action by checking the text changes.  More rigorous input 
                  validation might be needed depending on the requirements.  For example, you could check the 
                  button\'s CSS properties to ensure they\'ve changed as expected.\n\n\nThis comprehensive plan 
                  ensures a robust and maintainable Playwright test, suitable for integration into a CI/CD pipeline.  
                  Remember to replace placeholders like the URL with your actual values.\n' additional_kwargs={} 
                  response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 
                  'STOP', 'safety_ratings': []} id='run-e04814d1-f553-4ace-8841-f816ab3cee68-0' usage_metadata={
                  'input_tokens': 7176, 'output_tokens': 1137, 'total_tokens': 8313, 'input_token_details': {
                  'cache_read': 0}}
        '''

        # 调用 step2code 方法
        result = generate_script.step2code(plan_text2)

        # 打印结果
        print("Generated Playwright Code:")
        print(result)


if __name__ == "__main__":
    unittest.main()
