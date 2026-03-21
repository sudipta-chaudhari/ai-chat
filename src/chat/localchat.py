from openai import OpenAI
# Import configuration constants (URLs, keys, and model settings) from a central config file """
from src.config import LLM_BASE_URL, LLM_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS

# Initialize the OpenAI client. 
# base_url is set to point to a local model endpoint (like Ollama or LocalAI) 
# instead of the default OpenAI cloud servers.

client = OpenAI(
    api_key=LLM_API_KEY,  # Local model doesn't require an API key. With real API key, read this from .env file
    base_url=LLM_BASE_URL  # Local model endpoint
)

def add_message(messages, role, content):
    """
    Formats and appends a new message to the conversation history.
    
    Args:
        messages (list): The list containing the chat history.
        role (str): The speaker's role ('system', 'user', or 'assistant').
        content (str): The actual text of the message.
    """
    message = {"role": role, "content": content}
    messages.append(message)

def chat(messages):
    """
    Sends the full conversation history to the LLM and retrieves the response.
    
    Args:
        messages (list): The full list of chat messages for context.
        
    Returns:
        str: The text content of the AI's response.
    """

    # Create a chat completion request using parameters defined in config.py
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        temperature=LLM_TEMPERATURE, # Controls randomness/creativity
        max_tokens=LLM_MAX_TOKENS # Limits the length of the generated output
    )

    # Extract and return only the text from the first completion choice
    return response.choices[0].message.content
