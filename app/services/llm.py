import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class LLMService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.8-flash"

    def generate_structured(self, prompt, schema):
        interaction = self.client.interactions.create(
            model=self.model,
            input=prompt,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": schema.model_json_schema(),
            },
            timeout=60,
        )

        return schema.model_validate_json(interaction.output_text)
