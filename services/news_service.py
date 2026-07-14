import os
import requests
from dotenv import load_dotenv
import requests
import trafilatura
from bs4 import BeautifulSoup
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
    
    def get_article(self, article):
        url = article["url"]

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=15
            )

            response.raise_for_status()

            extracted_text = trafilatura.extract(
                response.text,
                include_comments=False,
                include_tables=False
            )

        except Exception:
            extracted_text = None

        # Fallback to NewsAPI content
        article_text = (
            extracted_text
            or article.get("content")
            or article.get("description")
            or ""
        )

        return {
            "url": url,
            "title": article.get("title", ""),
            "text": article_text,
            "top_image": article.get("urlToImage", ""),
            "authors": [article.get("author")] if article.get("author") else [],
            "publish_date": article.get("publishedAt"),
            "source": article.get("source", {}).get("name", ""),
        }