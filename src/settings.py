# ==================== LLM (Large Language Model) Configuration ====================
# Settings class that encapsulates all LLM configuration

class Settings:
    """
    Encapsulates all LLM configuration settings.
    Centralizes model parameters, API endpoint, and behavior controls.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str,
        temperature: float,
        max_tokens: int,
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
        # self._base_url = base_url # Internal storage
        # self._api_key = api_key
        # self._model = model 
        # self._temperature = temperature
        # self._max_tokens = max_tokens
        
        # Use property setters
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    # Properties for accessing and modifying private fields
    @property
    def base_url(self) -> str:
        """Getter: allows reading the value."""
        return self._base_url

    @base_url.setter
    def base_url(self, value: str) -> None:
        """Setter: allows adding validation logic."""
        if not value.startswith("http"):
            raise ValueError("Base URL must start with http or https")
        self._base_url = value

    @property
    def api_key(self) -> str:
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        self._api_key = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def temperature(self) -> float:
       return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        if not (0.0 <= value <= 1.0):
            raise ValueError("Temperature must be between 0.0 and 1.0")
        self._temperature = value

    @property
    def max_tokens(self) -> int:
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, value: int) -> None:
        self._max_tokens = value


# ==================== End of Settings class ====================
