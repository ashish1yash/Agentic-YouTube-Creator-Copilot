from app.workflow.state import WorkflowState
from app.workflow.youtube_node import process_youtube
from app.workflow.content_node import analyze_content
from app.workflow.seo_node import analyze_seo

state = WorkflowState(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# YouTube
state = process_youtube(state)


# Content Analysis
state = analyze_content(state)


# SEO Analysis
state = analyze_seo(state)


print("===== SEO NODE RESULT =====")

print("\nMain Topic:")
print(state.content_analysis.main_topic)

print("\nPrimary Keywords:")

for keyword in state.seo_analysis.primary_keywords:
    print("-", keyword)

print("\nSecondary Keywords:")

for keyword in state.seo_analysis.secondary_keywords:
    print("-", keyword)

print("\nHashtags:")

for hashtag in state.seo_analysis.hashtags:
    print("-", hashtag)
