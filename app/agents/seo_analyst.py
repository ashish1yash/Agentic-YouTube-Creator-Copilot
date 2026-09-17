from pathlib import Path

from app.models.schemas import ContentAnalysis, SEOAnalysis
from app.services.llm import LLMService


class SEOAnalyst:

    def __init__(self):
        self.llm = LLMService()

        prompt_path = Path(__file__).parent.parent / "prompts" / "seo_analyst.txt"

        self.prompt_template = prompt_path.read_text(encoding="utf-8")

    def analyze(self, content: ContentAnalysis) -> SEOAnalysis:

        prompt = self.prompt_template.format(
            main_topic=content.main_topic,
            subtopics=", ".join(content.subtopics),
            target_audience=content.target_audience,
            content_category=content.content_category,
            content_intent=content.content_intent,
            key_points=", ".join(content.key_points),
        )

        return self.llm.generate_structured(
            prompt=prompt,
            schema=SEOAnalysis,
        )
