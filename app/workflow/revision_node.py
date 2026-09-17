from app.agents.content_writer import ContentWriter
from app.workflow.state import WorkflowState


def revise_content(state: WorkflowState) -> WorkflowState:

    if not state.content_analysis:
        raise ValueError("Content analysis is missing.")

    if not state.seo_analysis:
        raise ValueError("SEO analysis is missing.")

    if not state.writer_output:
        raise ValueError("Writer output is missing.")

    if not state.validation:
        raise ValueError("Validation result is missing.")

    feedback = "\n".join(state.validation.issues + state.validation.suggestions)

    writer = ContentWriter()

    revised_output = writer.revise(
        content=state.content_analysis,
        seo=state.seo_analysis,
        writer=state.writer_output,
        feedback=feedback,
    )

    state.writer_output = revised_output
    state.revision_count += 1

    return state
