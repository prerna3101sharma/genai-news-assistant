import json
import re

from services.llm import LLMService
from prompts.entity_prompt import ENTITY_PROMPT


class EntityExtractor:

    def __init__(self):
        self.llm = LLMService()

    def _clean_response(self, response: str) -> str:
        """Remove markdown code fences and surrounding whitespace."""

        response = response.strip()

        response = re.sub(
            r"^```(?:json)?",
            "",
            response,
            flags=re.IGNORECASE
        )

        response = re.sub(
            r"```$",
            "",
            response
        )

        return response.strip()

    def _recover_entities(self, response: str):
        """
        Recover as many JSON objects as possible even if
        the response is truncated.
        """

        entities = []

        # Find every complete {...}
        matches = re.findall(r"\{[^{}]*\}", response, re.DOTALL)

        for obj in matches:
            try:
                entity = json.loads(obj)

                if (
                    isinstance(entity, dict)
                    and "text" in entity
                    and "label" in entity
                ):
                    entities.append(entity)

            except Exception:
                continue

        return entities

    def extract_entities(self, article_text):

        prompt = ENTITY_PROMPT.format(
            text=article_text[:2500]   # reduce context
        )

        response = self.llm.generate(prompt)

        response = self._clean_response(response)

        # --------------------------
        # First attempt
        # --------------------------

        try:

            entities = json.loads(response)

        except Exception:

            # --------------------------
            # Second attempt
            # Recover partial JSON
            # --------------------------

            entities = self._recover_entities(response)

        # --------------------------
        # Remove duplicates
        # --------------------------

        unique = []
        seen = set()

        for entity in entities:

            key = (
                entity["text"].strip(),
                entity["label"].strip()
            )

            if key not in seen:

                seen.add(key)
                unique.append(entity)

        return unique