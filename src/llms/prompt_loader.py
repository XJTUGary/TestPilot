import json
import os


class PromptLoader:
    def __init__(self, file_path):
        """
        Initialize the PromptLoader with a JSON file path.

        Args:
            file_path (str): Path to the JSON file containing prompts.
        """
        self.file_path = os.path.join(os.path.dirname(__file__), '..', file_path)
        self.prompts = self._load_prompts()

    def _load_prompts(self):
        """Load prompts from the JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            raise RuntimeError(f"Failed to load prompts from {self.file_path}: {e}")

    def get_prompt(self, prompt_name, **kwargs):
        """
        Retrieve a prompt and replace placeholders with provided arguments.

        Args:
            prompt_name (str): The key of the prompt in the JSON file.
            kwargs: Placeholder values to replace in the prompt.

        Returns:
            str: The processed prompt with placeholders replaced.
        """
        prompt = self.prompts.get(prompt_name)
        if not prompt:
            raise ValueError(f"Prompt '{prompt_name}' not found in {self.file_path}")
        return prompt.format(**kwargs)