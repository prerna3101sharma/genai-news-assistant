from services.llm import LLMService
from prompts.qa_prompt import QA_PROMPT


class QAEngine:

    def __init__(self):
        self.llm = LLMService()

    def answer_question(self, article: dict, question: str) -> str:
        context = f"""
            Title: {article.get("title", "Unknown")}

            Author: {", ".join(article.get("authors", [])) if article.get("authors") else "Unknown"}

            Source: {article.get("source", "Unknown")}

            Published Date: {article.get("publish_date", "Unknown")}

            URL: {article.get("url", "")}

            Article:

            {article.get("text", "")[:6000]}
            """
        # article_text = article_text[:6000]

        prompt = QA_PROMPT.format(
            article=context,
            question=question
        )

        try:
            return self.llm.generate(prompt)
        except Exception as e:
            return f"Error generating answer: {str(e)}"