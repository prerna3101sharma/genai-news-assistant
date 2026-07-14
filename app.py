from services.news_service import NewsService

news = NewsService()

articles = news.search_news("Artificial Intelligence")

for article in articles:
    print(article["title"])
    print(article["url"])
    print("-" * 50)