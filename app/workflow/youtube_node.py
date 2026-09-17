from app.tools.youtube import extract_video_id, get_transcript
from app.tools.transcript_cleaner import TranscriptCleaner
from app.workflow.state import WorkflowState


def process_youtube(state: WorkflowState) -> WorkflowState:

    # Extract video ID
    video_id = extract_video_id(state.url)

    # Retrieve transcript
    raw_transcript = get_transcript(video_id)

    # Clean transcript
    cleaner = TranscriptCleaner()
    clean_transcript = cleaner.clean(raw_transcript)

    # Update workflow state
    state.video_id = video_id
    state.raw_transcript = raw_transcript
    state.clean_transcript = clean_transcript

    return state
