from app.workflow.state import WorkflowState

state = WorkflowState(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


print("URL:", state.url)
print("Video ID:", state.video_id)
print("Raw Transcript:", state.raw_transcript)
print("Content Analysis:", state.content_analysis)
