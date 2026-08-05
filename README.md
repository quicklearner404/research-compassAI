
# Research Compass AI

An AI-powered research assistant that autonomously explores technical topics using an agentic workflow.

Instead of simply answering questions, Research Compass AI plans a research strategy, searches multiple knowledge sources, evaluates the retrieved information, and produces a structured research report with references.

The project combines a modern React interface with a FastAPI backend and a multi-tool AI agent built using SmolAgents and LiteLLM.

---

# Features

### Intelligent Research Agent

* Autonomous multi-step reasoning
* Dynamic tool selection
* Multi-source information retrieval
* Structured research reports
* Markdown rendering
* Session-based conversations

---

### Research Tools

The agent can use multiple tools during a conversation:

* arXiv paper search
* GitHub repository search
* DuckDuckGo web search
* Tutorial discovery
* Learning resource recommendations

The agent decides which tools to call instead of relying on hardcoded workflows.

---

### Modern Chat Interface

* React + Vite frontend
* Real-time conversation interface
* Optimistic message rendering
* Automatic scrolling
* Markdown support
* Persistent research sessions

---

### Conversation Management

* Create unlimited research sessions
* Resume previous conversations
* SQLite-backed chat history
* Automatically generated session titles

---

### LLM Integration

The backend communicates with language models through LiteLLM.

This abstraction allows switching providers without changing application logic.

Supported providers include:

* OpenAI-compatible APIs
* Groq
* Ollama
* Future providers

---

# Tech Stack

## Frontend

* React
* Vite
* Tailwind CSS
* React Router

---

## Backend

* FastAPI
* SQLite
* Uvicorn

---

## AI

* SmolAgents
* LiteLLM
* Hugging Face
* Groq (current provider)

---

## External APIs

* arXiv API
* GitHub API
* DuckDuckGo Search

---

# Architecture

```text
                 User
                   │
                   ▼
         React + Vite Frontend
                   │
          REST API Requests
                   │
                   ▼
            FastAPI Backend
                   │
          Conversation Manager
                   │
                   ▼
           Research Agent
          (SmolAgents)
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
  arXiv Tool   GitHub Tool   Web Search Tool
      │            │            │
      └────────────┼────────────┘
                   │
          Gather Research Results
                   │
                   ▼
         LiteLLM Provider Layer
                   │
                   ▼
          Language Model (Groq)
                   │
                   ▼
        Structured Markdown Report
                   │
                   ▼
            React Chat Interface
```

---

# Project Structure

```
research-compassAI/

backend/
│
├── agent.py
├── api.py
├── database.py
├── tool_decider.py
├── tool_result.py
├── services/
├── utils/
└── requirements.txt

frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── context/
│
└── package.json

assets/
tests/

README.md
.env.example
```

---

# Backend Workflow

When a user submits a research question:

1. The frontend sends the query to the FastAPI backend.

2. The backend stores the user message in SQLite.

3. The agent analyzes the question.

4. The agent determines which tools are required.

5. Each selected tool retrieves relevant information.

6. The collected evidence is passed to the language model through LiteLLM.

7. The model generates a structured research response.

8. The response is saved to the conversation database.

9. The frontend fetches and displays the completed conversation.

---

# Design Principles

The project is divided into independent layers.

### Frontend

Responsible only for user interaction and presentation.

---

### Backend API

Handles authentication, session management, and communication between the frontend and the AI agent.

---

### Research Agent

Acts as the reasoning engine.

It decides:

* what information is required,
* which tools to call,
* when to stop searching,
* and how to synthesize the final response.

---

### Tools

Each tool performs one specialized task.

Examples:

* arXiv search
* GitHub search
* Web search

Tools remain independent so new capabilities can be added without modifying the agent.

---

### LiteLLM Provider Layer

Separates application logic from model providers.

Changing from Groq to Ollama or OpenAI only requires updating configuration rather than rewriting the backend.

---

# Future Improvements

* Streaming responses
* Multi-provider fallback
* Citation verification
* Saved reports
* PDF export
* User authentication
* Conversation sharing
* Research summarization

---

# Deployment

Frontend:

* Vercel

Backend:

* Render

Database:

* SQLite (development)
* PostgreSQL (future)

---

# License

MIT License

---



