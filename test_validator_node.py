from app.models.schemas import (
    ContentAnalysis,
    SEOAnalysis,
    WriterOutput,
)
from app.workflow.state import WorkflowState
from app.workflow.validator_node import validate_content

content = ContentAnalysis(
    main_topic="Artificial Intelligence",
    subtopics=[
        "Machine Learning",
        "Deep Learning",
        "Generative AI",
    ],
    target_audience="Students and AI enthusiasts",
    content_category="Education",
    content_intent="Explain artificial intelligence concepts",
    key_points=[
        "AI enables machines to perform intelligent tasks",
        "Machine learning is a subset of AI",
        "Deep learning uses neural networks",
    ],
    important_facts=[
        "Machine learning is a branch of artificial intelligence",
    ],
)

seo = SEOAnalysis(
    primary_keywords=[
        "artificial intelligence",
        "AI",
    ],
    secondary_keywords=[
        "machine learning",
        "deep learning",
    ],
    long_tail_keywords=[
        "artificial intelligence explained",
    ],
    tags=[
        "AI",
        "Machine Learning",
        "Deep Learning",
    ],
    hashtags=[
        "#AI",
        "#MachineLearning",
    ],
)

writer = WriterOutput(
    title="Artificial Intelligence Explained",
    description="An introduction to artificial intelligence, machine learning, and deep learning.",
    hook="What exactly is artificial intelligence?",
    call_to_action="Subscribe for more AI content.",
)


state = WorkflowState(url="https://www.youtube.com/watch?v=test")

state.content_analysis = content
state.seo_analysis = seo
state.writer_output = writer


state = validate_content(state)


print("\n===== VALIDATION =====")
print("Valid:", state.validation.is_valid)
print("Grounding Score:", state.validation.grounding_score)
print("Keyword Relevance:", state.validation.keyword_relevance_score)
print("Completeness:", state.validation.completeness_score)

print("\nIssues:")
for issue in state.validation.issues:
    print("-", issue)

print("\nSuggestions:")
for suggestion in state.validation.suggestions:
    print("-", suggestion)
