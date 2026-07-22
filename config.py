from dotenv import load_dotenv
import os

project_root = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(project_root, ".env"))
load_dotenv(os.path.join(project_root, "backend", ".env"), override=False)

# ========= LLM =========
MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "huggingface")
#========== Development =========
USE_MOCK_LLM = True
# ========= APIs =========
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "openai/gpt-oss-120b"
# ========= Search =========
MAX_PAPERS = 3
MAX_REPOS = 3
MAX_RESOURCES = 3

# ========= App =========
APP_NAME = "Research Compass AI"
VERSION = "0.1.0"