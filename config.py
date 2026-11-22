import os

from dotenv import load_dotenv

project_root = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(project_root, ".env"))
load_dotenv(os.path.join(project_root, "backend", ".env"), override=False)


def _env_bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


# ========= LLM =========
# One of: huggingface | groq | ollama
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "huggingface")

MODEL_ID = os.getenv("HF_MODEL_ID", "Qwen/Qwen2.5-72B-Instruct")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Maximum tool-calling steps the agent may take per question.
AGENT_MAX_STEPS = int(os.getenv("AGENT_MAX_STEPS", "1"))

# ========= Development =========
# Return canned responses instead of calling an LLM (used by tests / CI).
USE_MOCK_LLM = _env_bool("USE_MOCK_LLM", False)

# ========= APIs =========
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ========= Search =========
MAX_PAPERS = 3
MAX_REPOS = 3
MAX_RESOURCES = 3

# ========= App =========
APP_NAME = "Research Compass AI"
VERSION = "0.1.0"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{os.path.join(project_root, 'research_compass.db')}",
)

# Comma-separated list of allowed frontend origins.
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]
