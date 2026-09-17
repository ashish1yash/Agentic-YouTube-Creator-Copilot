from app.workflow.state import WorkflowState
from app.workflow.youtube_node import process_youtube

state = WorkflowState(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


state = process_youtube(state)


print("===== YOUTUBE NODE RESULT =====")

print("\nURL:")
print(state.url)

print("\nVideo ID:")
print(state.video_id)

print("\nRaw Transcript Length:")
print(len(state.raw_transcript))

print("\nClean Transcript Length:")
print(len(state.clean_transcript))

print("\nClean Transcript Preview:")
print(state.clean_transcript[:500])
