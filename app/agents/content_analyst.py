from pathlib import Path

from app.models.schemas import ContentAnalysis
from app.services.llm import LLMService


class ContentAnalyst:

    def __init__(self):
        self.llm = LLMService()

        prompt_path = Path(__file__).parent.parent / "prompts" / "content_analyst.txt"

        self.prompt_template = prompt_path.read_text(encoding="utf-8")

    def analyze(self, transcript: str) -> ContentAnalysis:

        prompt = self.prompt_template.format(transcript=transcript)

        return self.llm.generate_structured(
            prompt=prompt,
            schema=ContentAnalysis,
        )
