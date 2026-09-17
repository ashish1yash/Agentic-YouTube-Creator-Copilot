from app.workflow.state import WorkflowState
from app.workflow.youtube_node import process_youtube
from app.workflow.content_node import analyze_content

state = WorkflowState(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# YouTube node
state = process_youtube(state)


# Content analysis node
state = analyze_content(state)


print("===== CONTENT NODE RESULT =====")

print("\nVideo ID:")
print(state.video_id)

print("\nMain Topic:")
print(state.content_analysis.main_topic)

print("\nCategory:")
print(state.content_analysis.content_category)

print("\nIntent:")
print(state.content_analysis.content_intent)

print("\nKey Points:")

for point in state.content_analysis.key_points:
    print("-", point)
