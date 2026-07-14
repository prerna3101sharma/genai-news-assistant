ENTITY_PROMPT = """
You are an NLP expert.

Extract all named entities from the article.

Return ONLY valid JSON.

Example:

[
    {{
        "text":"OpenAI",
        "label":"Organization"
    }},
    {{
        "text":"Sam Altman",
        "label":"Person"
    }}
]

Article:

{text}
"""