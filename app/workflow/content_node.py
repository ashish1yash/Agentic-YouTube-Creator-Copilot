from app.agents.content_analyst import ContentAnalyst
from app.workflow.state import WorkflowState


def analyze_content(state: WorkflowState) -> WorkflowState:

    if not state.clean_transcript:
        raise ValueError("Clean transcript is missing.")

    analyst = ContentAnalyst()

    analysis = analyst.analyze(state.clean_transcript)

    state.content_analysis = analysis

    return state
