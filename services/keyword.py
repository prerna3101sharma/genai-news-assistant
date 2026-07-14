from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

class KeywordExtractor:
    def __init__(self):
        embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cpu"
        )

        self.model = KeyBERT(model=embedding_model)

    def extract_keywords(self, article_text, top_n=10):
        keywords = self.model.extract_keywords(
            article_text,
            keyphrase_ngram_range=(1, 2),
            stop_words="english",
            top_n=top_n
        )

        return [keyword for keyword, score in keywords]