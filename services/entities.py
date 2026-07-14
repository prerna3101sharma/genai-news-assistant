import json

from services.llm import LLMService
from prompts.entity_prompt import ENTITY_PROMPT


class EntityExtractor:

    def __init__(self):
        self.llm = LLMService()

    def extract_entities(self, article_text):

        prompt = ENTITY_PROMPT.format(
            text=article_text[:6000]
        )

        response = self.llm.generate(prompt)

        try:
            return json.loads(response)
        except Exception:
            return []