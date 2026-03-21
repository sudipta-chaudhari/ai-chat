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
git clone https://github.com/yourusername/ai-chat.git
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

The project uses a centralized configuration file to manage all LLM settings:

### Default Configuration

Configuration is managed in [`src/config.py`](src/config.py):

```python
# LLM API Endpoint
LLM_BASE_URL = "http://127.0.0.1:1234/v1"

# API Key (for local models, this can be arbitrary)
LLM_API_KEY = "not needed"

# Model to use
LLM_MODEL = "liquid/lfm2.5-1.2b"

# Response randomness (0.0 = deterministic, 1.0 = creative)
LLM_TEMPERATURE = 0.7

# Maximum response length in tokens
LLM_MAX_TOKENS = 512
```

### Customizing Configuration

Edit [`src/config.py`](src/config.py) to modify parameters:

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| `LLM_BASE_URL` | API endpoint URL | `http://127.0.0.1:1234/v1` | Any valid URL |
| `LLM_API_KEY` | Authentication key | `"not needed"` | String |
| `LLM_MODEL` | Model identifier | `liquid/lfm2.5-1.2b` | Model name |
| `LLM_TEMPERATURE` | Response creativity | `0.7` | 0.0 - 1.0 |
| `LLM_MAX_TOKENS` | Max response tokens | `512` | 1 - model limit |

### Using Environment Variables (Recommended for Production)

For better security, use environment variables instead of hardcoding API keys:

**On Windows (PowerShell):**
```powershell
$env:LLM_API_KEY = "your-api-key-here"
$env:LLM_BASE_URL = "your-endpoint-here"
```

**On macOS/Linux (Bash):**
```bash
export LLM_API_KEY="your-api-key-here"
export LLM_BASE_URL="your-endpoint-here"
```

Then update `src/config.py` to read from environment variables:
```python
import os
LLM_API_KEY = os.getenv("LLM_API_KEY", "not needed")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:1234/v1")
```

---

## Usage

### Running the Application

```bash
python main.py
```

### Example Interaction

```
Ask a question (or 'exit' to quit): What is machine learning?
Answer: Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed...

Ask a question (or 'exit' to quit): Can you give a simpler explanation?
Answer: Sure! Machine learning is when computers learn patterns from data and make predictions without being told exactly how to do it...

Ask a question (or 'exit' to quit): exit
```

### Commands

| Command | Action |
|---------|--------|
| Type any question | Send message to the chat |
| `exit` | Quit the application |

---

## Project Structure

```
ai-chat/
├── main.py                          # Application entry point
├── pyproject.toml                   # Project metadata and dependencies
├── README.md                        # This file
├── src/
│   ├── __pycache__/                # Python bytecode cache
│   ├── config.py                   # Configuration settings
│   └── chat/
│       ├── __pycache__/            # Python bytecode cache
│       └── localchat.py            # Chat logic and LLM integration
└── openai_chat.egg-info/           # Package metadata
```

### File Descriptions

- **[main.py](main.py)**: Implements the CLI interface and main application loop
- **[src/config.py](src/config.py)**: Centralized configuration management
- **[src/chat/localchat.py](src/chat/localchat.py)**: Core chat functionality and OpenAI client initialization
- **[pyproject.toml](pyproject.toml)**: Project metadata, version, and dependencies

---

## Advanced Configuration

### Setting Up with OpenAI's API

To use OpenAI's official API instead of a local service:

1. Create an OpenAI account at https://openai.com
2. Generate an API key from your account dashboard
3. Update `src/config.py`:

```python
LLM_BASE_URL = "https://api.openai.com/v1"
LLM_API_KEY = "your-api-key-here"  # Keep this private, add to .env file!!
LLM_MODEL = "gpt-3.5-turbo"  # or "gpt-4"
```

### Setting Up with Local LLM Services

#### Using LM Studio

1. Download from https://lmstudio.ai
2. Download a model in the LM Studio interface
3. Start the local server (usually runs on `http://127.0.0.1:1234`)
4. Keep default configuration in `src/config.py`

#### Using Ollama

1. Install from https://ollama.ai
2. Pull a model: `ollama pull llama2`
3. Models run on `http://127.0.0.1:11434` by default
4. Update `src/config.py`:

```python
LLM_BASE_URL = "http://127.0.0.1:11434/v1"
LLM_MODEL = "llama2"
```

### Optimizing for Different Use Cases

**For Factual/Precise Responses:**
```python
LLM_TEMPERATURE = 0.1  # Lower temperature for consistency
LLM_MAX_TOKENS = 256   # Shorter responses
```

**For Creative Responses:**
```python
LLM_TEMPERATURE = 0.9  # Higher temperature for variety
LLM_MAX_TOKENS = 1024  # Longer responses
```

**For Balanced Performance:**
```python
LLM_TEMPERATURE = 0.7  # Moderate creativity
LLM_MAX_TOKENS = 512   # Moderate length
```

---

## Troubleshooting

### Issue: "Connection refused" error

**Cause**: LLM service is not running or URL is incorrect

**Solution**:
1. Verify the LLM service is running on the configured URL
2. Check `LLM_BASE_URL` in `src/config.py`
3. Test the endpoint with: `curl http://127.0.0.1:1234/v1/models`

### Issue: "Authentication failed" error

**Cause**: Invalid or missing API key

**Solution**:
1. For local models: Set `LLM_API_KEY = "not needed"` in `src/config.py`
2. For OpenAI: Verify your API key is correct and active
3. Check for typos or extra whitespace in the key

### Issue: Slow responses or timeouts

**Cause**: Model is processing-intensive or network issues

**Solution**:
1. Reduce `LLM_MAX_TOKENS` in `src/config.py`
2. Lower `LLM_TEMPERATURE` for simpler processing
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
1. Verify the model name in `LLM_MODEL`
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
- 🐛 **Issues**: Report bugs on the [GitHub Issues page](https://github.com/yourusername/ai-chat/issues)
- 💬 **Discussions**: Join conversations in [GitHub Discussions](https://github.com/yourusername/ai-chat/discussions)

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
