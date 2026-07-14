import os
import requests
from dotenv import load_dotenv
from newspaper import Article
from utils.preprocessing import TextPreprocessor

load_dotenv()


class NewsService:
    BASE_URL = os.getenv("NEWS_API_ENDPOINT")

    def search_news(self, query):
        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 10,
            "apiKey": os.getenv("NEWS_API_KEY"),
        }

        response = requests.get(self.BASE_URL, params=params)

        response.raise_for_status()

        return response.json()["articles"]
    
    def get_article(self, url):
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = TextPreprocessor.clean_text(article.text[:6000])
            return {
                "title": article.title,
                "authors": article.authors,
                "publish_date": article.publish_date,
                "text": text,
                "top_image": article.top_image,
            }

        except Exception as e:
            print(e)
            return None