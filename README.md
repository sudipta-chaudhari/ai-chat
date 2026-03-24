# OpenAI Chatbot using Python

A Python-based conversational AI chat application that seamlessly integrates with OpenAI models or compatible local LLM services. This project allows you to have interactive conversations while maintaining full conversation history.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Advanced Configuration](#advanced-configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

✨ **Core Features:**
- 💬 Interactive conversational CLI interface with persistent message history
- 🔌 Flexible LLM backend support (OpenAI, local models, or compatible endpoints)
- ⚙️ Highly configurable model parameters (temperature, max tokens, etc.)
- 🛡️ Secure API key management with environment variable support
- 📝 Conversation context preservation for multi-turn interactions
- 🚀 Simple and intuitive command-line interface

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager (comes with Python)
- **Git**: For cloning the repository (optional)

### Optional Requirements

Depending on your LLM backend choice:
- **Local LLM Service**: If using local models, ensure a compatible LLM service is running (e.g., LM Studio, Ollama, or similar)
- **OpenAI API Key**: If using OpenAI's API directly instead of a local service

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sudipta-chaudhari/ai-chat.git
cd ai-chat
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -e .
```

Or install dependencies manually:

```bash
pip install "openai>=1.3.0"
```

---

## Configuration

The project uses a `Settings` class to manage all LLM configuration parameters. Configuration is defined in [`src/settings.py`](src/settings.py).

### Default Configuration

The default settings are defined as constants in [`src/settings.py`](src/settings.py):

```python
DEFAULT_BASE_URL = "http://127.0.0.1:1234/v1"
DEFAULT_API_KEY = "not needed"
DEFAULT_MODEL = "liquid/lfm2.5-1.2b"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512
```

### Customizing Configuration

You can customize settings in [`src/settings.py`](src/settings.py) by modifying the `Settings` class default parameters, or override them in [`main.py`](main.py) before initializing the `ChatClient`:

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| `base_url` | API endpoint URL | `DEFAULT_BASE_URL` | Any valid URL |
| `api_key` | Authentication key | `DEFAULT_API_KEY` | String |
| `model` | Model identifier | `DEFAULT_MODEL` | Model name |
| `temperature` | Response creativity | `DEFAULT_TEMPERATURE` | 0.0 - 1.0 |
| `max_tokens` | Max response tokens | `DEFAULT_MAX_TOKENS` | 1 - model limit |

### Using Environment Variables (Recommended for Production)

For better security, especially for API keys, use environment variables. Update [`src/settings.py`](src/settings.py) to read from environment:

```python
import os

class Settings:
    def __init__(
        self,
        base_url: str = os.getenv("LLM_BASE_URL", "http://127.0.0.1:1234/v1"),
        api_key: str = os.getenv("LLM_API_KEY", "not needed"),
        model: str = os.getenv("LLM_MODEL", "liquid/lfm2.5-1.2b"),
        temperature: float = float(os.getenv("LLM_TEMPERATURE", "0.7")),
        max_tokens: int = int(os.getenv("LLM_MAX_TOKENS", "512")),
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
```

Then set environment variables:

**On Windows (PowerShell):**
```powershell
$env:LLM_API_KEY = "your-api-key-here"
$env:LLM_BASE_URL = "https://api.openai.com/v1"
$env:LLM_MODEL = "gpt-3.5-turbo"
```

**On macOS/Linux (Bash):**
```bash
export LLM_API_KEY="your-api-key-here"
export LLM_BASE_URL="https://api.openai.com/v1"
export LLM_MODEL="gpt-3.5-turbo"
```

---

## Usage

### Running the Application

```bash
python main.py
```

### Example Interaction

```
🤖 Chat initialized with model: liquid/lfm2.5-1.2b
Type 'exit' to quit, 'clear' to clear conversation history
--------------------------------------------------

You: What is Machine Learning? Explain in one sentence. 
Assistant: Machine learning is a subset of artificial intelligence that enables computers to learn patterns from data without being explicitly programmed.

You: Write one more sentence.
Assistant: Machine learning empowers systems to improve their performance on tasks through experience and data analysis.

You: exit
Goodbye!
```

### Commands

| Command           | Action                       |
|-------------------|------------------------------|
| Type any question | Send message to the chat     |
| `clear`           | Clear conversation history   |
| `exit`            | Quit the application         |

---

## Project Structure

```
ai-chat/
├── main.py                          # Application entry point
├── pyproject.toml                   # Project metadata and dependencies
├── README.md                        # This file is primary documentation for a project
├── src/
│   ├── __init__.py                 # Package initialization
│   ├── settings.py                 # Configuration settings (Settings class)
│   └── chat/
│       ├── __init__.py             # Package initialization
│       ├── chat_client.py          # OpenAI client wrapper
│       └── chat_session.py         # Conversation history management
└── openai_chat.egg-info/           # Package metadata (generated)
```

### File Descriptions

- **[main.py](main.py)**: Implements the CLI interface and main application loop
- **[src/settings.py](src/settings.py)**: `Settings` class with LLM configuration parameters
- **[src/chat/chat_client.py](src/chat/chat_client.py)**: `ChatClient` class that handles API communication
- **[src/chat/chat_session.py](src/chat/chat_session.py)**: `ChatSession` class for managing conversation history
- **[pyproject.toml](pyproject.toml)**: Project metadata, version, and dependencies

---

## Advanced Configuration

### Setting Up with OpenAI's API

To use OpenAI's official API instead of a local service:

1. Create an OpenAI account at https://openai.com
2. Generate an API key from your account dashboard
3. Update `src/settings.py` (or override in `main.py`):

```python
# Example of overriding in main.py, before initializing ChatClient:
settings.base_url = "https://api.openai.com/v1"
settings.api_key = "your-api-key-here"  # IMPORTANT: For production, use environment variables as shown above!
settings.model = "gpt-3.5-turbo"  # or "gpt-4"
```

### Setting Up with Local LLM Services

#### Using LM Studio

1. Download from https://lmstudio.ai
2. Download a model in the LM Studio interface
3. Start the local server (usually runs on `http://127.0.0.1:1234`)
4. Keep default configuration in `src/settings.py` (or override in `main.py`).

#### Using Ollama

1. Install from https://ollama.ai
2. Pull a model: `ollama pull llama2`
3. Models run on `http://127.0.0.1:11434` by default
4. Update `src/settings.py` (or override in `main.py`):

```python
# Example of overriding in main.py, before initializing ChatClient:
settings.base_url = "http://127.0.0.1:11434/v1"
settings.model = "llama2"
```

### Optimizing for Different Use Cases

You can optimize the model's behavior by adjusting `temperature` and `max_tokens` settings. These are defined as default values in [`src/settings.py`](src/settings.py) and can be overridden in [`main.py`](main.py) before initializing the `ChatClient`.

**For Factual/Precise Responses:**
```python
# Default in src/settings.py or override in main.py before initializing ChatClient:
settings.temperature = 0.1  # Lower temperature = more deterministic/focused
settings.max_tokens = 256   # Shorter responses for conciseness
```

**For Creative Responses:**
```python
# Default in src/settings.py or override in main.py before initializing ChatClient:
settings.temperature = 0.9  # Higher temperature = more creative/varied
settings.max_tokens = 1024  # Longer responses for richer content
```

**For Balanced Performance (Default):**
```python
# Default settings in src/settings.py:
settings.temperature = 0.7  # Moderate creativity and consistency
settings.max_tokens = 512   # Balanced response length
```

---

## Troubleshooting

### Issue: "Connection refused" error

**Cause**: LLM service is not running or URL is incorrect

**Solution**:
1. Verify the LLM service is running on the configured URL
2. Check `base_url` in `src/settings.py`
3. Test the endpoint with: `curl http://127.0.0.1:1234/v1/models`

### Issue: "Authentication failed" error

**Cause**: Invalid or missing API key

**Solution**:
1. For local models: Set `api_key = "not needed"` in `src/settings.py`
2. For OpenAI: Verify your API key is correct and active
3. Check for typos or extra whitespace in the key

### Issue: Slow responses or timeouts

**Cause**: Model is processing-intensive or network issues

**Solution**:
1. Reduce `max_tokens` in `src/settings.py`
2. Lower `temperature` for simpler processing
3. Check network connectivity
4. Try a smaller or faster model

### Issue: ImportError for 'openai' module

**Cause**: Dependencies not installed

**Solution**:
```bash
pip install -e .
# or
pip install "openai>=1.3.0"
```

### Issue: Model not found error

**Cause**: Specified model is not available

**Solution**:
1. Verify the model name in `model`
2. Ensure the model is downloaded/installed on your system
3. Check available models: `ollama list` or your service's model manager

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** with clear, descriptive commits
4. **Test thoroughly** before submitting
5. **Push to your fork**: `git push origin feature/your-feature-name`
6. **Submit a Pull Request** with a description of your changes

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions
- Keep functions focused and single-purpose

---

## License

This project is open-source and available under the MIT License. See LICENSE file for details.

---

## Support & Contact

- 📧 **Email**: Not provided
- 🐛 **Issues**: Report bugs on the [GitHub Issues page](https://github.com/sudipta-chaudhari/ai-chat/issues)
- 💬 **Discussions**: Join conversations in [GitHub Discussions](https://github.com/sudipta-chaudhari/ai-chat/discussions)

---

## Changelog

### Version 0.1.0 (Current)
- Initial release
- Basic CLI interface
- OpenAI API integration
- Local LLM support
- Conversation history management

---

## Acknowledgments

- Built with [OpenAI Python SDK](https://github.com/openai/openai-python)
- Compatible with local LLM services like LM Studio and Ollama
- Inspired by modern AI chat interfaces

---

**Last Updated**: March 2026
