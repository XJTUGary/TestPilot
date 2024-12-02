from llms.llm_provider import LLMProvider
from llms.prompt_loader import PromptLoader
from langchain.prompts import PromptTemplate
from data_models import _get_test_cases_parser
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
        self.test_cases_parser = _get_test_cases_parser()
        self.html_to_test_cases_prompt = PromptTemplate(
            input_variables=["WEB_CONTENT"],
            partial_variables={"format_test_cases": self.test_cases_parser.get_format_instructions()},
            template=('''Assign yourself as a quality assurance engineer.
            Read this code and design comprehensive tests to test the UI of this HTML. 
            Break it down into 5-10 separate modules and identify the possible things to test for each module. 
            For each module, also identify which tests should be checked repeatedly 
            (e.g., after every code change, every build, etc.).
            Ensure the following are considered:
            - Input validation is thoroughly tested.
            - Avoid using if-else steps in the test design.
            - Consider session timeouts and their handling.
            - Test all actionable items (e.g., buttons, links).
            
            Return the output in the following JSON format:
            {format_test_cases}
            CONTENT: ```{WEB_CONTENT}```
            '''
                      )
        )

        self.html_to_test_cases_user_prompt = PromptTemplate(
            input_variables=["WEB_CONTENT", "USER_PROMPT"],
            partial_variables={"format_test_cases": self.test_cases_parser.get_format_instructions()},
            template=('''Assign yourself as a quality assurance engineer.
            Read this code and design comprehensive tests to test the UI of this HTML. 
            This is user's prompt: {USER_PROMPT}. 
            Break it down into 5-10 separate modules and identify the possible things to test for each module. 
            For each module, also identify which tests should be checked repeatedly 
            (e.g., after every code change, every build, etc.).
            Ensure the following are considered:
            - Input validation is thoroughly tested.
            - Avoid using if-else steps in the test design.
            - Consider session timeouts and their handling.
            - Test all actionable items (e.g., buttons, links).
            
            Return the output in the following JSON format:
            {format_test_cases}
            CONTENT: ```{WEB_CONTENT}```
            '''
                      )
        )

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

                return response.text
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
            if user_prompt:
                prompt = self.html_to_test_cases_user_prompt.format(USER_PROMPT=user_prompt, WEB_CONTENT=html)
            else:
                prompt = self.html_to_test_cases_prompt.format(WEB_CONTENT=html)
            messages = [
                ("system", system_prompt),
                ("human", prompt),
            ]
            response = self.llm_provider.llm.invoke(messages)
            test_cases = self.test_cases_parser.parse(response.content)
            return test_cases, html if test_cases else "Failed to generate Test Cases."
        except Exception as e:
            print(f"Error in html2cases: {e}")
            return f"Error: {e}"

    def generateTestCases(self, url, user_prompt=""):
        html = self.getHTML(url)
        cases = self.html2cases(html, user_prompt)
        return cases
