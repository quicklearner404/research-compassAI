# Research Compass AI

Research Compass AI is an agent-based application that helps users explore AI research topics. Given a topic, the agent autonomously discovers relevant research papers, open-source implementations, and learning resources before generating a structured learning roadmap.

> **Status:**  In Development

---

# Project Structure

```
research-compass-ai/
│
├── agent/
├── agent_tools/
├── services/
├── utils/
├── models/
├── assets/
├── tests/
├── .streamlit/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# Directory Overview

## `agent/`

Contains the application's core agent logic.

| File         | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `agent.py`   | Creates and runs the research agent.               |
| `planner.py` | Handles planning and execution flow between tools. |
| `prompts.py` | Stores system prompts and agent instructions.      |

---

## `agent_tools/`

Contains all tools available to the agent.

Each tool performs one task and exposes a consistent interface.

| File               | Purpose                                    |
| ------------------ | ------------------------------------------ |
| `base_tool.py`     | Base interface implemented by every tool.  |
| `arxiv_tool.py`    | Retrieves research papers from arXiv.      |
| `github_tool.py`   | Searches GitHub for relevant repositories. |
| `learning_tool.py` | Finds tutorials and educational resources. |
| `search_tool.py`   | Performs general web searches.             |

---

## `services/`

Contains application services that process or format data independently of the agent.

| File           | Purpose                               |
| -------------- | ------------------------------------- |
| `roadmap.py`   | Builds structured learning roadmaps.  |
| `formatter.py` | Formats raw outputs for presentation. |

---

## `utils/`

Shared helper functions and constants.

| File           | Purpose                                    |
| -------------- | ------------------------------------------ |
| `helpers.py`   | Utility functions used across the project. |
| `constants.py` | Shared constants and default values.       |

---

## `models/`

Reserved for future data models and schemas.

---

## `tests/`

Unit tests for individual modules.

---

## `assets/`

Static project assets.

Examples include screenshots, diagrams, and demonstration media.

---

## `.streamlit/`

Configuration files for the Streamlit application.

---

# Root Files

| File               | Purpose                                                    |
| ------------------ | ---------------------------------------------------------- |
| `app.py`           | Streamlit application entry point.                         |
| `config.py`        | Loads application configuration and environment variables. |
| `requirements.txt` | Python dependencies.                                       |
| `.env.example`     | Template for required environment variables.               |
| `README.md`        | Project documentation.                                     |

---

# Design Principles

The project is organized around four independent layers:

* **User Interface** — Handles user interaction.
* **Agent** — Plans actions and decides which tools to use.
* **Tools** — Execute external operations such as searching arXiv or GitHub.
* **Services** — Process and format results before presentation.

This separation keeps components modular, reusable, and easy to extend.

---

# Planned Features

* Agent-based research exploration
* arXiv integration
* GitHub repository discovery
* Learning resource recommendations
* Personalized learning roadmap
* Streamlit interface
* Hugging Face Spaces deployment

---

# License

MIT License
