
# 🧠 LangChain OpenAI Chat Agent

This project implements an **interactive AI chatbot** using [LangChain](https://python.langchain.com), [LangGraph](https://github.com/langchain-ai/langgraph), and [OpenAI GPT models](https://platform.openai.com).
It automatically **falls back to a cheaper model** (`gpt-3.5-turbo`) if `gpt-4o` quota or rate limits are exceeded.

---

## ✨ Features

* ✅ Interactive **command-line chatbot**
* ✅ Built with **LangChain** and **LangGraph**
* ✅ Uses **OpenAI GPT-4o** by default
* ✅ Automatic fallback to **GPT-3.5-Turbo** on quota/rate-limit errors
* ✅ Easy to extend with custom tools

---

## 🛠️ Requirements

* Python 3.9+
* OpenAI API key

Install dependencies:

```bash
pip install langchain langchain-openai langgraph python-dotenv openai
```

---

## ⚙️ Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a `.env` file** in the project root with your OpenAI API key:

   ```
   OPENAI_API_KEY=sk-your_openai_api_key_here
   ```

3. **Run the script**

   ```bash
   python main.py
   ```

---

## 🖥️ Usage

* After running `python main.py`, you’ll see:

  ```
  ✅ Using GPT-4o
  Welcome!
  Ask me anything (type 'quit' to exit):
  ```

* Type your question:

  ```
  You : What is LangChain?
  ```

* The assistant will stream its response:

  ```
  Assistant : LangChain is a framework for building applications with LLMs...
  ```

* Type `quit` to exit.

---

## 🔧 Extending with Tools

You can add custom tools by defining them with `@tool`.
Example:

```python
from langchain.tools import tool

@tool
def calculator(a: float, b: float) -> str:
    """Useful for math operations."""
    return f"The sum of {a} and {b} is {a + b}"
```

Then add the tool to the `tools` list before creating the agent:

```python
tools = [calculator]
agent_executor = create_react_agent(model, tools)
```

---

## 📂 Project Structure

```
.
├── main.py          # Main chatbot script
├── .env             # Environment variables (add your OpenAI API key here)
└── README.md        # Project documentation
```

---

## ⚠️ Notes

* Make sure you have an **active OpenAI plan**.
* Free trial credits can run out quickly; the script will automatically switch to `gpt-3.5-turbo` if quota is exceeded.

---

## 📜 License

This project is licensed under the MIT License.


Would you like me to also add a **“How it works” diagram** (like a simple flow chart in the README)? It makes it look much more professional on GitHub.
