# 🤖 LLM Chat Tutor Agent

Here I have tried to solve a simple probelm of making a **conversational AI tutor** powered by **LLaMA 3** (via [Ollama]) that can:

✅ Answer questions from **PDF course books** (RAG) . You as a tutor or student can upload study material from your course content for example CS771 for passing your midsems :P ! 
🌐 Retrieve information from the **web** (DuckDuckGo) . Duh its needed if you wanna score above avg.
📖 Pull facts from **Wikipedia**. Because one can never forget the OG wikipedia
🧮 Perform **Python calculations and code execution** . Needed for actual coding probelms ( trust me you will get most of these in IITK courses)
🧠 Maintain **chat history and context** . Because a tutor learns your ways and history :) like most IIT Kanpur Profs!

---

## 🔧 Features

| Feature               | Source                   | Method                             |
|----------------------|--------------------------|------------------------------------|
| Course Q&A           | Local PDF vector search  | FAISS + Sentence Embeddings (RAG) |
| General Info         | DuckDuckGo Web Search    | LangChain Tool                     |
| Factual Queries      | Wikipedia Search         | LangChain Tool                     |
| Math/Programming     | Python Tool              | Python REPL                        |
| Conversational Memory| Chat History             | LangChain Memory                   |

---

## 📁 Directory Structure

ollama_chat-tutor-agent_project/
├── agents/
│ └── chat_agent.py # Main conversational agent setup
├── data/
│ ├── raw_pdfs/ # PDF books or materials
│ └── db/ # FAISS vector store (auto-created)
├── retriever/
│ ├── vector_store.py # FAISS-based PDF retriever
│ └── web_retrievers.py # Web + Wikipedia retrievers
├── scripts/
│ ├── index_data.py # Index PDF content into vector store
│ └── chat_loop.py # CLI chatbot loop
├── requirements.txt # Python dependencies
└── README.md # This file

## Project Architecture
        ┌────────────┐
        │ User Input │
        └─────┬──────┘
              │
              ▼
     ┌────────────────────┐
     │  Conversational Agent (LLaMA3.2) │
     └────┬─────────────┬────┬────┬──┘
          │             │    │    │
          ▼             ▼    ▼    ▼
 ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
 │ PDF Search  │ │ Web Search  │ │ Wikipedia    │ │ Python REPL  │
 │ (FAISS RAG) │ │ (DuckDuckGo)│ │ Retriever     │ │ Code Exec.   │
 └─────────────┘ └─────────────┘ └─────────────┘ └──────────────┘
          │             │    │    │
          └─────────────┴────┴────┘
                        │
                        ▼
              ┌────────────────────┐
              │ Generated Response │
              └────────────────────┘


---

## 🚀 Getting Started

### 1. Install Dependencies

Make sure you have Python 3.10+ and FAISS-compatible system. And install ollama on your local PC for running LLM llama3.2

```bash
pip install -r requirements.txt
ollama run llama3.2
```
### 2. Add Pdfs in data/raw_pdfs/ and index them by
```bash
python scripts/index_data.py
```
### 3. Start the agent
```bash
python scripts/chat_loop.py
```