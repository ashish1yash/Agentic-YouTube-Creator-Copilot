from app.agents.validator import Validator
from app.workflow.state import WorkflowState


def validate_content(state: WorkflowState) -> WorkflowState:
    if not state.content_analysis:
        raise ValueError("Content analysis is missing.")

    if not state.seo_analysis:
        raise ValueError("SEO analysis is missing.")

    if not state.writer_output:
        raise ValueError("Writer output is missing.")

    validator = Validator()

    validation = validator.validate(
        content=state.content_analysis,
        seo=state.seo_analysis,
        writer=state.writer_output,
    )

    state.validation = validation

    return state
