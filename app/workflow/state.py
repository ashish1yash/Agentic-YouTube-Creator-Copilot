from dataclasses import dataclass
from typing import Optional

from app.models.schemas import (
    ContentAnalysis,
    SEOAnalysis,
    WriterOutput,
    ValidationResult,
)


@dataclass
class WorkflowState:

    url: str

    video_id: Optional[str] = None

    raw_transcript: Optional[str] = None

    clean_transcript: Optional[str] = None

    content_analysis: Optional[ContentAnalysis] = None

    seo_analysis: Optional[SEOAnalysis] = None

    writer_output: Optional[WriterOutput] = None

    validation: Optional[ValidationResult] = None

    revision_count: int = 0
    max_revisions: int = 2
