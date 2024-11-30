from langchain_google_genai import ChatGoogleGenerativeAI

GEMINI_API_KEY = 'AIzaSyBN4ol-3RTcn9Xg28IJLErm0eO0wZAm7v0'


class LLMProvider:
    """
    LLMProvider is a wrapper for initializing and using Google Gemini LLM.
    """

    def __init__(self, temperature=0.0):
        """
        Initialize the LLMProvider with the given model.

        Args:
            temperature (float): Sampling temperature for generation.
                     Higher values (e.g., 0.8) produce more diverse results.
        """
        self.model_name = "gemini-1.5-flash"
        self.transport = "rest"
        self.temperature = temperature
        self.llm = None
        self._initialize_model()

    def _initialize_model(self):
        """Initialize the Gemini model."""
        try:
            self.llm = ChatGoogleGenerativeAI(
                model=self.model_name,
                temperature=self.temperature,
                google_api_key=GEMINI_API_KEY,
                transport=self.transport,
            )
            print(f"Model '{self.model_name}' initialized successfully.")
            return
        except Exception as e:
            print(f"Error initializing model: {e}")


# Example usage:
if __name__ == "__main__":
    llm_provider = LLMProvider()
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm_provider.llm.invoke(messages)
    print(ai_msg)
