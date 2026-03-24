# ChatClient handles communication with the LLM API

from openai import OpenAI
from src.settings import settings


class ChatClient:
    """
    Handles communication with the LLM API.
    Sends messages to the model and retrieves responses using configured settings.
    """

    def __init__(self, settings_obj: object = None):
        """
        Initialize the chat client with LLM configuration.

        Args:
            settings_obj: Settings object containing API configuration.
                         If None, uses the default settings instance from settings module.
        """
        if settings_obj is None:
            settings_obj = settings

        self.settings = settings_obj

        # Initialize the OpenAI client.
        # base_url is set to point to a local model endpoint (like LMStudio or Ollama or LocalAI)
        # instead of the default OpenAI cloud servers.
        self.client = OpenAI(
            api_key=self.settings.api_key,  # Local model doesn't require an API key
            base_url=self.settings.base_url,  # Local model endpoint
        )

    def send(self, messages: list) -> str:
        """
        Sends the full conversation history to the LLM and retrieves the response.

        Args:
            messages (list): The full list of chat messages for context.

        Returns:
            str: The text content of the AI's response, or an error message.
        """
        try:
            # Create a chat completion request using parameters from settings
            response = self.client.chat.completions.create(
                model=self.settings.model,
                messages=messages,
                temperature=self.settings.temperature,  # Controls randomness/creativity
                max_tokens=self.settings.max_tokens,  # Limits the length of the generated output
            )

            # Extract and return only the text from the first completion choice
            return response.choices[0].message.content

        except Exception as e:
            return f"Error: {str(e)}"
