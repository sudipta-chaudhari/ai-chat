from openai import OpenAI
from src.config import LLM_BASE_URL, LLM_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS

# Initialize the OpenAI client pointing to your local model
client = OpenAI(
    api_key=LLM_API_KEY,  # Local model doesn't require an API key. With real API key, read this from .env file
    base_url=LLM_BASE_URL  # Local model endpoint
)

def add_message(messages, role, content):
    message = {"role": role, "content": content}
    messages.append(message)

def chat(messages):
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS
    )
    return response.choices[0].message.content
