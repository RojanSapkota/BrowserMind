
# BrowserMind

<div align="center">

<img src="https://img.shields.io/badge/🌐-BrowserMind-7F77DD?style=flat" />


**Run Tasks in Autopilot.**
Any model. Minimal setup.

[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/rojansapkota/BrowserMind?style=flat&logo=github)](https://github.com/rojansapkota/BrowserMind)
[![Providers](https://img.shields.io/badge/LLM_Providers-5-7F77DD?style=flat)](README.md)

[Features](#-features) · [Quick Start](#-quick-start) · [Configuration](#-configuration) · [Examples](#-usage-examples)

</div>

---

## 🎯 Overview

**BrowserMind** is a browser automation agent built on top of [browser-use](https://github.com/browser-use/browser-use) — giving you a single interface to run any browser task using the LLM of your choice. Point it at a task, pick a model, and let it run.

> Form automation · Data scraping · Complex workflows · Headless by default · 5 LLM providers

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Multi-LLM Support** | Works with Anthropic (Claude), OpenAI (GPT-4), Groq, Google (Gemini), and Ollama |
| **Speed Optimized** | Built-in speed optimization for fast task completion with minimal steps |
| **Easy Setup** | Minimal configuration—just set your API keys and go |
| **Headless Browsing** | Efficient headless browser automation out of the box |
| **Vision Disabled** | Faster execution without vision capabilities (easily toggleable) |
| **Error Handling** | Graceful fallbacks and error management |
| **Extensible Tools** | Built on Browser-Use's comprehensive tool ecosystem |

---

## 🚀 Quick Start

### 1. **Clone & Install**

```bash
git clone https://github.com/rojansapkota/BrowserMind.git
cd BrowserMind
pip install -r requirements.txt
```

### 2. **Set Your API Key**

Create a `.env` file in the project root:

```bash
# Choose one or more providers
GROQ_API_KEY=your_groq_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

### 3. **Run Your First Task**

```bash
python main.py
```

When prompted, enter a task:
```
Enter your task for the agent: Find the latest AI news on Hacker News
```

The agent will automatically browse and complete the task for you.

---

## 💾 Installation

### Prerequisites

- Python [3.11.9](https://www.python.org/downloads/release/python-3119/)

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/rojansapkota/BrowserMind.git
cd BrowserMind

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Chromium (if not already installed)
# Browser-Use handles this automatically, but you can manually install:
# python -m playwright install chromium

# 4. Set up your environment variables
cp .env.example .env  # Create from template (optional)
# Edit .env with your API keys
```

---

## ⚙️ Configuration

### Supported LLM Providers

| Provider | Setup | Model |
|----------|-------|-------|
| **Groq** | Set `GROQ_API_KEY` | `meta-llama/llama-4-scout-17b-16e-instruct` |
| **Anthropic** | Set `ANTHROPIC_API_KEY` | `claude-3-5-sonnet-20240620` |
| **OpenAI** | Set `OPENAI_API_KEY` | `gpt-4.1` |
| **Google** | Set `GOOGLE_API_KEY` | `gemini-2.0-flash-lite` |
| **Ollama** | Run locally via Ollama | `llama3.2:latest` (customizable) |

### Environment Variables

```env
# API Keys
GROQ_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here

# Ollama (for local models)
OLLAMA_BASE_URL=http://localhost:11434
```

### Customization Options

Edit `main.py` to customize:

```python
# Browser window size
window_size={'width': 1280, 'height': 720}

# Page load wait time
minimum_wait_page_load_time=0.1

# Wait between actions
wait_between_actions=0.1

# Temperature (0 = deterministic, higher = more creative)
temperature=0.0
```

---

## 📖 Usage Examples

### Basic Task Execution

```python
from main import run_agent
import asyncio

# Simple task
asyncio.run(run_agent("Find the current Bitcoin price", provider='groq'))

# Use different providers
asyncio.run(run_agent("Fill out this form", provider='anthropic'))
asyncio.run(run_agent("Scrape product listings", provider='openai'))
```

### Programmatic Usage

```python
import asyncio
from main import initialize_agent

async def automated_workflow():
    query = "Navigate to google.com and search for 'Browser Mind'"
    agent, browser_session = initialize_agent(query, provider='groq')
    
    try:
        result = await agent.run()
        print(f"Task completed: {result}")
    finally:
        await browser_session.close()

asyncio.run(automated_workflow())
```

### Common Use Cases

- **Form Filling**: Automatically complete and submit web forms
- **Data Scraping**: Extract structured data from websites
- **Research**: Gather information from multiple sources
- **Monitoring**: Watch for changes and alerts
- **Automation**: Repetitive browser tasks

---

## 🔧 Advanced Configuration

### Custom System Message

```python
CUSTOM_PROMPT = """
Your custom instructions here.
Focus on speed and accuracy.
"""

agent = Agent(
    task=query,
    llm=llm,
    browser_session=browser_session,
    extend_system_message=CUSTOM_PROMPT
)
```

### Using Different Ollama Models

```bash
# Pull a model first
ollama pull mistral

# Then use it in main.py
return ChatOllama(model='mistral')
```

---

## 📊 Troubleshooting

| Issue | Solution |
|-------|----------|
| **API Key Error** | Ensure your `.env` file is in the project root and API key is valid |
| **Browser Won't Open** | Check if Chromium is installed; run `playwright install chromium` |
| **Timeout Errors** | Increase `minimum_wait_page_load_time` in the configuration |
| **Module Not Found** | Run `pip install -r requirements.txt` again |

---

## 🎓 Learn More

- **Browser-Use Documentation**: [docs.browser-use.com](https://docs.browser-use.com)
- **Browser-Use GitHub**: [github.com/browser-use/browser-use](https://github.com/browser-use/browser-use)
- **Playwright Documentation**: [playwright.dev](https://playwright.dev)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- Report bugs via [Issues](https://github.com/rojansapkota/BrowserMind/issues)
- Submit pull requests with improvements
- Share your use cases and examples

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

If you find Browser Mind helpful, please consider:

<div align="center">

[![Wise](https://img.shields.io/badge/Wise-00B9FF?style=for-the-badge&logo=wise&logoColor=white)](https://rojansapkota.com.np/wise) 
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/payrojan) 
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/rojansapkota) 
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://rojansapkota.com.np)

</div>

<div align="center">

**Made with ❤️ for the AI automation community**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/rojansapkota)
[![Twitter](https://img.shields.io/twitter/follow/rojansapkota?style=flat&logo=twitter&logoColor=white)](https://twitter.com/rojansapkota)

</div>
