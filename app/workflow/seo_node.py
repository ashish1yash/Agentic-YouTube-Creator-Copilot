from app.agents.seo_analyst import SEOAnalyst
from app.workflow.state import WorkflowState


def analyze_seo(state: WorkflowState) -> WorkflowState:

    if not state.content_analysis:
        raise ValueError("Content analysis is missing.")

    seo_analyst = SEOAnalyst()

    seo_analysis = seo_analyst.analyze(state.content_analysis)

    state.seo_analysis = seo_analysis

    return state
