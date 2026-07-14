ENTITY_PROMPT = """
You are an NLP expert.

Extract ONLY the 15 most important named entities.

Return ONLY valid JSON.

Do not explain anything.

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