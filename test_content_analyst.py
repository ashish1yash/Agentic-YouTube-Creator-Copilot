from app.tools.youtube import extract_video_id, get_transcript
from app.tools.transcript_cleaner import TranscriptCleaner
from app.agents.content_analyst import ContentAnalyst

# YouTube video
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


# 1. Extract video ID
video_id = extract_video_id(url)

print("Video ID:", video_id)


# 2. Retrieve transcript
raw_transcript = get_transcript(video_id)

print("Raw transcript retrieved.")
print("Raw transcript length:", len(raw_transcript))


# 3. Clean transcript
cleaner = TranscriptCleaner()

clean_transcript = cleaner.clean(raw_transcript)

print("Clean transcript length:", len(clean_transcript))


# 4. Analyze content using LLM
analyst = ContentAnalyst()

analysis = analyst.analyze(clean_transcript)


# 5. Display result
print("\n===== CONTENT ANALYSIS =====")

print("Main Topic:", analysis.main_topic)

print("\nSubtopics:")
for topic in analysis.subtopics:
    print("-", topic)

print("\nTarget Audience:")
print(analysis.target_audience)

print("\nContent Category:")
print(analysis.content_category)

print("\nContent Intent:")
print(analysis.content_intent)

print("\nKey Points:")
for point in analysis.key_points:
    print("-", point)

print("\nImportant Facts:")
for fact in analysis.important_facts:
    print("-", fact)
