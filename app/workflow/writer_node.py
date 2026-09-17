from app.agents.content_writer import ContentWriter
from app.workflow.state import WorkflowState


def generate_content(state: WorkflowState) -> WorkflowState:

    if not state.content_analysis:
        raise ValueError("Content analysis is missing.")

    if not state.seo_analysis:
        raise ValueError("SEO analysis is missing.")

    writer = ContentWriter()

    writer_output = writer.write(
        content=state.content_analysis,
        seo=state.seo_analysis,
    )

    state.writer_output = writer_output

    return state
