import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:4b")