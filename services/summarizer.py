from services.llm import LLMService
from prompts.summary_prompt import SUMMARY_PROMPT


class Summarizer:

    def __init__(self):
        self.llm = LLMService()

    def summarize(self, article_text):
        prompt = SUMMARY_PROMPT.format(
            text=article_text
        )

        try:
            return self.llm.generate(prompt)
        except Exception as e:
            return f"Error generating summary: {e}"