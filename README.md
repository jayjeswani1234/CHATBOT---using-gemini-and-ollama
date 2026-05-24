# AI Chatbot with LangChain + Ollama + Streamlit

A simple AI chatbot built using **LangChain**, **Streamlit**, and **Ollama** running lightweight local LLMs like **TinyLlama** or **Phi3 Mini**.

---

# Features

* Streamlit Web UI
* LangChain Prompt Templates
* Local LLM using Ollama
* No OpenAI API required
* Lightweight models for low-RAM laptops
* LangSmith tracing support

---

# Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* TinyLlama / Phi3 Mini

---

# Project Structure

```bash
GEN_aI/
│
├── lec4/
│   ├── olama.py
│   ├── chatbot.py
│   ├── .env
│
├── .venv/
│
├── requirements.txt
└── README.md
```

---

# Installation Guide

## 1. Clone the Project

```bash
git clone <your-repo-link>
cd GEN_aI
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate venv:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install langchain-core
pip install python-dotenv
```

Optional:

```bash
pip install langsmith
```

---

# Install Ollama

Download Ollama:

* Windows/Mac/Linux:

  [https://ollama.com/download](https://ollama.com/download)

Check installation:

```bash
ollama --version
```

---

# Download Lightweight Model

Recommended for low RAM systems:

## TinyLlama

```bash
ollama run tinyllama
```

OR

## Phi3 Mini

```bash
ollama run phi3:mini
```

Avoid using `llama2` on systems with less than 8GB RAM.

---

# Environment Variables

Create a `.env` file:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=my-chatbot
```

---

# Streamlit Chatbot Code

## olama.py

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

st.title("AI Chatbot with Ollama")

input_text = st.text_input("Ask something")

llm = Ollama(model="tinyllama")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
```

---

# Run the Project

Start Ollama first:

```bash
ollama run tinyllama
```

Open another terminal:

```bash
streamlit run olama.py
```

---

# Common Errors & Fixes

## 1. `streamlit not recognized`

Run:

```bash
python -m streamlit run olama.py
```

---

## 2. `No module named langchain_community`

Install:

```bash
pip install langchain-community
```

---

## 3. `No space left on device`

Free some disk space and reinstall packages.

---

## 4. `model requires more system memory`

Use smaller models:

```bash
ollama run tinyllama
```

or

```bash
ollama run phi3:mini
```

---

# Recommended Models

| Model     | RAM Usage | Speed  | Quality |
| --------- | --------- | ------ | ------- |
| tinyllama | Very Low  | Fast   | Basic   |
| phi3:mini | Low       | Medium | Good    |
| llama2    | High      | Slow   | Better  |

---

# Future Improvements

* Chat history
* Voice assistant
* PDF chatbot
* RAG pipeline
* Multi-model support
* Deployment on cloud

---

# Author

Jay Jeswani
B.Tech CSE Student | VIT Bhopal

---
