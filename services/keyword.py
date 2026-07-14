import json

from services.llm import LLMService
from prompts.keyword_prompt import KEYWORD_PROMPT


class KeywordExtractor:

    def __init__(self):
        self.llm = LLMService()

    def extract_keywords(self, article_text):

        prompt = KEYWORD_PROMPT.format(
            text=article_text[:6000]
        )

        response = self.llm.generate(prompt)

        try:
            return json.loads(response)
        except Exception:
            # Fallback if model returns comma-separated text
            return [
                keyword.strip()
                for keyword in response.split(",")
                if keyword.strip()
            ]