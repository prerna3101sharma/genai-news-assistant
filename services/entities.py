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
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, article_text):

        doc = self.nlp(article_text)

        entities = []

        for entity in doc.ents:
            entities.append({
                "text": entity.text,
                "label": LABEL_MAP.get(entity.label_, entity.label_)
            })

        return entities