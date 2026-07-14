from services.llm import LLMService

llm = LLMService()

response = llm.generate(
    "Explain Large Language Models in 50 words."
)

print(response)