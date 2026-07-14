from services.llm import LLMService
from prompts.sentiment_prompt import SENTIMENT_PROMPT


class SentimentAnalyzer:
    def __init__(self):
        self.llm = LLMService()

    def analyze_sentiment(self, article_text: str) -> str:
        # Prevent sending extremely long articles
        article_text = article_text[:6000]

        prompt = SENTIMENT_PROMPT.format(text=article_text)

        try:
            return self.llm.generate(prompt)
        except Exception as e:
            return f"Error generating sentiment analysis: {str(e)}"