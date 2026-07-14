import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

class LLMService:
    def __init__(self):
        self.client = InferenceClient(
            api_key=os.getenv("HF_TOKEN")
        )
        self.model = os.getenv("HF_MODEL")

    def generate(self, prompt: str):
        completion = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_tokens=600,

            temperature=0.3,
        )

        return completion.choices[0].message.content