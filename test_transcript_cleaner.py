from app.tools.youtube import extract_video_id, get_transcript
from app.tools.transcript_cleaner import TranscriptCleaner

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Step 1: Extract video ID
video_id = extract_video_id(url)

print("Video ID:", video_id)

# Step 2: Get raw transcript
raw_transcript = get_transcript(video_id)

print("\nRaw transcript:")
print(raw_transcript[:500])

# Step 3: Clean transcript
cleaner = TranscriptCleaner()

clean_transcript = cleaner.clean(raw_transcript)

print("\nClean transcript:")
print(clean_transcript[:500])
