from services.news_service import NewsService
from services.sentiment import SentimentAnalyzer
from services.summarizer import Summarizer
from services.keyword import KeywordExtractor
from services.entities import EntityExtractor
from services.qa_engine import QAEngine

qa = QAEngine()

news = NewsService()
summarizer = Summarizer()
sentiment_analyzer = SentimentAnalyzer()
keywordExtractor = KeywordExtractor()
extractor = EntityExtractor()

articles = news.search_news("Artificial Intelligence")

article = news.get_article(articles[0]["url"])

summary = summarizer.summarize(article["text"])

sentiment  = sentiment_analyzer.analyze_sentiment(article["text"])

keywords = keywordExtractor.extract_keywords(article["text"])

entities = extractor.extract_entities(article["text"])

answer = qa.answer_question(
    article["text"],
    "What is the CEO's salary?"
)


print(summary)
print("\n\n")
print(sentiment)
print("\n\n")
print(keywords)
print("\n\n")
print(entities)
print("\n\n")
print(answer)

