from llms.llm_provider import LLMProvider
from llms.prompt_loader import PromptLoader
import requests
import time

class GenerateTestCases:
    def __init__(self, llm_provider=None):
        """
        Initialize the GenerateScript class with an LLMProvider instance.

        Args:
            llm_provider (LLMProvider): The LLM provider for generating scripts. If None, initializes a default one.
        """
        self.llm_provider = llm_provider or LLMProvider()

    def getHTML(self, url, retries=3, delay=0):
        """
        Get HTML from given url.
        """
        attempt = 0
        while attempt < retries:
            try:
                response = requests.get(url)
                response.raise_for_status()

                response.encoding = response.apparent_encoding

                return response
            except requests.RequestException as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                attempt += 1
                time.sleep(delay)
        raise RuntimeError(f"Failed to fetch HTML from {url} after {retries} attempts.")

    def html2cases(self, html, user_prompt):
        """
        Convert HTML、system prompt and user prompt to test cases.
        """
        try:
            if not html:
                print("HTML content is empty.")
                return []
            loader = PromptLoader('llms/prompts.json')
            system_prompt = loader.get_prompt("PLAYWRIGHT_CODE_SYSTEM_PROMPT")
            if(user_prompt == ""):
                prompt = loader.get_prompt("HTML_TO_TEST_CASES_PROMPT", WEB_CONTENT=html)
            else:
                prompt = loader.get_prompt("HTML_TO_TEST_CASES_USER_PROMPT", USER_PROMPT=user_prompt, WEB_CONTENT=html)
            messages = [
                ("system", system_prompt),
                ("human", prompt),
            ]
            response = self.llm_provider.llm.invoke(messages)
            return response if response else "Failed to generate Test Cases."
        except Exception as e:
            print(f"Error in html2cases: {e}")
            return f"Error: {e}"

    def generateTestCases(self, url, user_prompt=""):
        html = self.getHTML(url)
        cases = self.html2cases(html, user_prompt)
        return cases