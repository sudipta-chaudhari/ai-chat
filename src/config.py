# ==================== LLM (Large Language Model) Configuration ====================
# These settings configure how the LLM is accessed and how it behaves

# BASE URL for the LLM API endpoint (running on local machine)
LLM_BASE_URL = "http://127.0.0.1:1234/v1"

# API KEY for the LLM API endpoint (running on local machine). With real API key, read this from .env file
LLM_API_KEY = "not needed"

# The specific model to use for embeddings
# This model converts text into vector representations for semantic search
LLM_MODEL = "liquid/lfm2.5-1.2b"

# Temperature controls randomness in LLM responses (0.0-1.0)
# Lower values (closer to 0) produce more deterministic/focused responses
# Higher values (closer to 1) produce more creative/varied responses
LLM_TEMPERATURE = 0.7

#The maximum number of tokens that can be generated in the chat completion. 
# This value can be used to control costs for text generated via API.
LLM_MAX_TOKENS = 512
