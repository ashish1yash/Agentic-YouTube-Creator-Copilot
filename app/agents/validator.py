from pathlib import Path

from app.models.schemas import (
    ContentAnalysis,
    SEOAnalysis,
    WriterOutput,
    ValidationResult,
)
from app.services.llm import LLMService


class Validator:

    def __init__(self):
        self.llm = LLMService()

        prompt_path = Path(__file__).parent.parent / "prompts" / "validator.txt"

        self.prompt_template = prompt_path.read_text(encoding="utf-8")

    def validate(
        self,
        content: ContentAnalysis,
        seo: SEOAnalysis,
        writer: WriterOutput,
    ) -> ValidationResult:

        prompt = self.prompt_template.format(
            main_topic=content.main_topic,
            subtopics=", ".join(content.subtopics),
            target_audience=content.target_audience,
            content_category=content.content_category,
            content_intent=content.content_intent,
            key_points=", ".join(content.key_points),
            primary_keywords=", ".join(seo.primary_keywords),
            secondary_keywords=", ".join(seo.secondary_keywords),
            long_tail_keywords=", ".join(seo.long_tail_keywords),
            title=writer.title,
            hook=writer.hook,
            description=writer.description,
            call_to_action=writer.call_to_action,
        )

        return self.llm.generate_structured(
            prompt=prompt,
            schema=ValidationResult,
        )
