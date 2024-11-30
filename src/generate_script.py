from llms.llm_provider import LLMProvider
from utils.prompt_loader import PromptLoader


class GenerateScript:
    """
    GenerateScript converts a textual plan into Playwright code using an LLMProvider.
    """

    def __init__(self, llm_provider=None):
        """
        Initialize the GenerateScript class with an LLMProvider instance.

        Args:
            llm_provider (LLMProvider): The LLM provider for generating scripts. If None, initializes a default one.
        """
        self.llm_provider = llm_provider or LLMProvider()

    def step2code(self, step_text):
        """
        Convert a plan to Playwright code using the LLM.

        Args:
            step_text (str): The textual description of the plan.

        Returns:
            str: The generated Playwright code, or an error message if generation fails.
        """
        try:
            loader = PromptLoader('llms/prompts.json')
            system_prompt = loader.get_prompt("PLAYWRIGHT_CODE_SYSTEM_PROMPT")
            prompt = loader.get_prompt("STEP_TO_PLAYWRIGHT_CODE_PROMPT", STEP_TEXT=step_text)
            messages = [
                ("system", system_prompt),
                ("human", prompt),
            ]
            response = self.llm_provider.llm.invoke(messages)
            return response if response else "Failed to generate Playwright code."
        except Exception as e:
            print(f"Error in plan2code: {e}")
            return f"Error: {e}"
