from app.models.schemas import ValidationResult
from app.workflow.state import WorkflowState
from app.workflow.decision import decide_next_step

# --------------------------------------------------
# CASE 1: Validation passed
# --------------------------------------------------

state = WorkflowState(url="https://www.youtube.com/watch?v=test")

state.validation = ValidationResult(
    is_valid=True,
    grounding_score=1.0,
    keyword_relevance_score=1.0,
    completeness_score=1.0,
    issues=[],
    suggestions=[],
)

print("CASE 1:", decide_next_step(state))


# --------------------------------------------------
# CASE 2: Validation failed, revision available
# --------------------------------------------------

state = WorkflowState(url="https://www.youtube.com/watch?v=test")

state.validation = ValidationResult(
    is_valid=False,
    grounding_score=0.6,
    keyword_relevance_score=0.8,
    completeness_score=0.7,
    issues=["Unsupported claim"],
    suggestions=["Remove the unsupported claim"],
)

state.revision_count = 0
state.max_revisions = 2

print("CASE 2:", decide_next_step(state))


# --------------------------------------------------
# CASE 3: Validation failed, maximum revisions reached
# --------------------------------------------------

state = WorkflowState(url="https://www.youtube.com/watch?v=test")

state.validation = ValidationResult(
    is_valid=False,
    grounding_score=0.6,
    keyword_relevance_score=0.8,
    completeness_score=0.7,
    issues=["Unsupported claim"],
    suggestions=["Remove the unsupported claim"],
)

state.revision_count = 2
state.max_revisions = 2

print("CASE 3:", decide_next_step(state))
