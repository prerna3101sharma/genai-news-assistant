from services.news_service import NewsService
from services.summarizer import Summarizer

news = NewsService()
summarizer = Summarizer()

articles = news.search_news("Artificial Intelligence")

article = news.get_article(articles[0]["url"])

summary = summarizer.summarize(article["text"])

print(summary)