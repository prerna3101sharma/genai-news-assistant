KEYWORD_PROMPT = """
You are an NLP expert.

Extract the 10 most important keywords from the news article.

Rules:
- Return ONLY valid JSON.
- Do not include any explanation.
- Each keyword should be concise.

Example:

[
    "Artificial Intelligence",
    "OpenAI",
    "Sam Altman",
    "Microsoft",
    "ChatGPT"
]

Article:

{text}
"""