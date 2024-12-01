from llms.llm_provider import LLMProvider
from llms.prompt_loader import PromptLoader


class GenerateTestStep:

    def __init__(self, llm_provider=None):

        self.llm_provider = llm_provider or LLMProvider()

    def case2step(self, test_description, url, web_content):
        try:
            loader = PromptLoader('llms/prompts.json')
            system_prompt = loader.get_prompt("PLAYWRIGHT_CODE_SYSTEM_PROMPT")
            prompt = loader.get_prompt(
                "TEST_DESCRIPTION_TO_STEP_PROMPT",
                TEST_DESCRIPTION=test_description,
                URL=url,
                WEB_CONTENT=web_content
            )
            messages = [
                ("system", system_prompt),
                ("human", prompt),
            ]
            response = self.llm_provider.llm.invoke(messages)
            return response if response else "Failed to generate test steps."
        except Exception as e:
            print(f"Error in case2step: {e}")
            return f"Error: {e}"
