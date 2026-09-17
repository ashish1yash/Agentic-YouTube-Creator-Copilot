from pydantic import BaseModel


class ContentAnalysis(BaseModel):
    main_topic: str
    subtopics: list[str]
    target_audience: str
    content_category: str
    content_intent: str
    key_points: list[str]
    important_facts: list[str]


class SEOAnalysis(BaseModel):
    primary_keywords: list[str]
    secondary_keywords: list[str]
    long_tail_keywords: list[str]
    tags: list[str]
    hashtags: list[str]


class WriterOutput(BaseModel):
    title: str
    description: str
    hook: str
    call_to_action: str


class ValidationResult(BaseModel):
    is_valid: bool
    grounding_score: float
    keyword_relevance_score: float
    completeness_score: float
    issues: list[str]
    suggestions: list[str]

