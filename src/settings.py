# ==================== LLM (Large Language Model) Configuration ====================
# Settings class that encapsulates all LLM configuration

# Default configuration constants
DEFAULT_BASE_URL = "http://127.0.0.1:1234/v1"
DEFAULT_API_KEY = "not needed"
DEFAULT_MODEL = "liquid/lfm2.5-1.2b"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512


class Settings:
    """
    Encapsulates all LLM configuration settings.
    Centralizes model parameters, API endpoint, and behavior controls.
    """


    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        api_key: str = DEFAULT_API_KEY,
        model: str = DEFAULT_MODEL,
        temperature: float = DEFAULT_TEMPERATURE,
        max_tokens: int = DEFAULT_MAX_TOKENS,
    ):
        """
        Initialize LLM configuration settings.

        Args:
            base_url (str): BASE URL for the LLM API endpoint (running on local machine)
            api_key (str): API KEY for the LLM API endpoint. With real API key, read from .env file, properties etc.
            model (str): The specific model to use for chat completions
            temperature (float): Controls randomness in LLM responses (0.0-1.0).
                                 Lower values (closer to 0) = more deterministic/focused
                                 Higher values (closer to 1) = more creative/varied
            max_tokens (int): Maximum number of tokens that can be generated in the chat completion.
                             Used to control costs for text generated via API.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens


# Create a default Settings instance for convenient access
settings = Settings()
