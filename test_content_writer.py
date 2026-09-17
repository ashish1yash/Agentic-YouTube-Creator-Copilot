from app.tools.youtube import extract_video_id, get_transcript
from app.tools.transcript_cleaner import TranscriptCleaner
from app.agents.content_analyst import ContentAnalyst
from app.agents.seo_analyst import SEOAnalyst
from app.agents.content_writer import ContentWriter

# YouTube video
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


# 1. Extract video ID
video_id = extract_video_id(url)

print("Video ID:", video_id)


# 2. Get transcript
raw_transcript = get_transcript(video_id)

print("Raw transcript retrieved.")
print("Raw transcript length:", len(raw_transcript))


# 3. Clean transcript
cleaner = TranscriptCleaner()

clean_transcript = cleaner.clean(raw_transcript)

print("Clean transcript length:", len(clean_transcript))


# 4. Content Analysis
content_analyst = ContentAnalyst()

content_analysis = content_analyst.analyze(clean_transcript)

print("\n===== CONTENT ANALYSIS =====")
print("Main Topic:", content_analysis.main_topic)
print("Category:", content_analysis.content_category)


# 5. SEO Analysis
seo_analyst = SEOAnalyst()

seo_analysis = seo_analyst.analyze(content_analysis)

print("\n===== SEO ANALYSIS =====")
print("Primary Keywords:")
for keyword in seo_analysis.primary_keywords:
    print("-", keyword)


# 6. Content Writer
writer = ContentWriter()

writer_output = writer.write(content=content_analysis, seo=seo_analysis)


# 7. Display generated content
print("\n===== GENERATED CONTENT =====")

print("\nTitle:")
print(writer_output.title)

print("\nHook:")
print(writer_output.hook)

print("\nDescription:")
print(writer_output.description)

print("\nCall To Action:")
print(writer_output.call_to_action)
