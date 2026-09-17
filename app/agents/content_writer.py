from pathlib import Path

from app.models.schemas import ContentAnalysis, SEOAnalysis, WriterOutput
from app.services.llm import LLMService


class ContentWriter:

    def __init__(self):
        self.llm = LLMService()

        prompt_path = Path(__file__).parent.parent / "prompts" / "content_writer.txt"

        self.prompt_template = prompt_path.read_text(encoding="utf-8")

    def write(
        self,
        content: ContentAnalysis,
        seo: SEOAnalysis,
    ) -> WriterOutput:

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
            tags=", ".join(seo.tags),
            hashtags=", ".join(seo.hashtags),
        )

        return self.llm.generate_structured(
            prompt=prompt,
            schema=WriterOutput,
        )
        
        def revise(
            self,
            content: ContentAnalysis,
            seo: SEOAnalysis,
            writer: WriterOutput,
            feedback: str,
        ) -> WriterOutput:

            prompt = f"""
Revise the existing YouTube content using the validator feedback.

CONTENT ANALYSIS
Main Topic:
{content.main_topic}

Subtopics:
{", ".join(content.subtopics)}

Target Audience:
{content.target_audience}

Content Intent:
{content.content_intent}

Key Points:
{", ".join(content.key_points)}


SEO INFORMATION
Primary Keywords:
{", ".join(seo.primary_keywords)}

Secondary Keywords:
{", ".join(seo.secondary_keywords)}

Long-tail Keywords:
{", ".join(seo.long_tail_keywords)}

Tags:
{", ".join(seo.tags)}

Hashtags:
{", ".join(seo.hashtags)}


CURRENT OUTPUT

Title:
{writer.title}

Hook:
{writer.hook}

Description:
{writer.description}

Call to Action:
{writer.call_to_action}


VALIDATOR FEEDBACK
{feedback}


REVISION RULES

- Fix every issue identified by the validator.
- Follow the validator suggestions where appropriate.
- Keep the content grounded in the content analysis.
- Do not introduce unsupported facts.
- Preserve relevant SEO keywords.
- Keep the same overall topic.
- Improve the existing output rather than unnecessarily rewriting everything.
"""

        return self.llm.generate_structured(
            prompt=prompt,
            schema=WriterOutput,
        )