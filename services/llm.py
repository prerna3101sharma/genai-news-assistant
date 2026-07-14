from langchain_ollama import ChatOllama
from config import OLLAMA_MODEL


class LLMService:
    def __init__(self):
        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            temperature=0.2
        )

    def generate(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response.content