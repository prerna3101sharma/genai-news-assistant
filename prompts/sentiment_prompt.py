SENTIMENT_PROMPT = """
You are an expert sentiment analysis assistant.

Analyze the following news article.

Return ONLY in the following format:

Sentiment: Positive / Negative / Neutral

Reason:
<One sentence>

Article:
{text}
"""