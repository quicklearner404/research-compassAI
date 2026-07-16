from dotenv import load_dotenv
import os

load_dotenv()

# ========= LLM =========
MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"

# ========= APIs =========
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# ========= Search =========
MAX_PAPERS = 3
MAX_REPOS = 3
MAX_RESOURCES = 3

# ========= App =========
APP_NAME = "Research Compass AI"
VERSION = "0.1.0"