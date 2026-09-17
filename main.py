from app.workflow.state import WorkflowState
from app.workflow.youtube_node import process_youtube
from app.workflow.content_node import analyze_content
from app.workflow.seo_node import analyze_seo
from app.workflow.writer_node import generate_content
from app.workflow.validator_node import validate_content
from app.workflow.revision_node import revise_content
from app.workflow.decision import decide_next_step


def run_workflow(url: str) -> WorkflowState:

    state = WorkflowState(url=url)

    print("\n[1] Processing YouTube video...")
    state = process_youtube(state)

    print("[2] Analyzing content...")
    state = analyze_content(state)

    print("[3] Analyzing SEO...")
    state = analyze_seo(state)

    print("[4] Generating content...")
    state = generate_content(state)

    while True:

        print("[5] Validating generated content...")
        state = validate_content(state)

        decision = decide_next_step(state)

        print(f"[6] Decision: {decision}")

        if decision == "end":
            break

        print(f"[7] Revising content " f"(revision {state.revision_count + 1})...")

        state = revise_content(state)

    return state


if __name__ == "__main__":

    url = input("Enter YouTube URL: ").strip()

    final_state = run_workflow(url)

    print("\n" + "=" * 60)
    print("FINAL OUTPUT")
    print("=" * 60)

    print("\nTitle:")
    print(final_state.writer_output.title)

    print("\nHook:")
    print(final_state.writer_output.hook)

    print("\nDescription:")
    print(final_state.writer_output.description)

    print("\nCall to Action:")
    print(final_state.writer_output.call_to_action)

    print("\n" + "=" * 60)
    print("VALIDATION")
    print("=" * 60)

    print("Valid:", final_state.validation.is_valid)
    print("Grounding:", final_state.validation.grounding_score)
    print("Keyword Relevance:", final_state.validation.keyword_relevance_score)
    print("Completeness:", final_state.validation.completeness_score)
    print("Revisions:", final_state.revision_count)
