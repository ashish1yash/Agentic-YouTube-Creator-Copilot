from app.workflow.state import WorkflowState


def decide_next_step(state: WorkflowState) -> str:
    if not state.validation:
        raise ValueError("Validation result is missing.")

    # Content passed validation
    if state.validation.is_valid:
        return "end"

    # Content failed, but revisions are still available
    if state.revision_count < state.max_revisions:
        return "revise"

    # Maximum revisions reached
    return "end"
