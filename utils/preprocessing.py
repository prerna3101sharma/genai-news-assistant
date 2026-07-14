import re


class TextPreprocessor:

    @staticmethod
    def clean_text(text):
        text = re.sub(r"http\S+", "", text)

        text = re.sub(r"\s+", " ", text)

        text = text.strip()

        return text