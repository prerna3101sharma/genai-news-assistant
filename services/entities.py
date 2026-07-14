import spacy

LABEL_MAP = {
    "PERSON": "Person",
    "ORG": "Organization",
    "GPE": "Location",
    "DATE": "Date",
    "TIME": "Time",
    "MONEY": "Money",
    "EVENT": "Event",
}

class EntityExtractor:

    def __init__(self):
        self.nlp = None

    def _load_model(self):
        if self.nlp is None:
            self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, article_text):

        self._load_model()

        doc = self.nlp(article_text)

        return [
            {
                "text": ent.text,
                "label": LABEL_MAP.get(ent.label_, ent.label_)
            }
            for ent in doc.ents
        ]