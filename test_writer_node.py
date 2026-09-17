from app.workflow.state import WorkflowState
from app.workflow.youtube_node import process_youtube
from app.workflow.content_node import analyze_content
from app.workflow.seo_node import analyze_seo
from app.workflow.writer_node import generate_content

state = WorkflowState(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# 1. YouTube
state = process_youtube(state)


# 2. Content Analysis
state = analyze_content(state)


# 3. SEO Analysis
state = analyze_seo(state)


# 4. Content Generation
state = generate_content(state)


print("===== WRITER NODE RESULT =====")

print("\nTitle:")
print(state.writer_output.title)

print("\nHook:")
print(state.writer_output.hook)

print("\nDescription:")
print(state.writer_output.description)

print("\nCall To Action:")
print(state.writer_output.call_to_action)
