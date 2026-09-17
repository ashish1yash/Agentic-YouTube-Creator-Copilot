from app.tools.youtube import extract_video_id, get_transcript

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

video_id = extract_video_id(url)

print("Video ID:", video_id)
print("\nFetching transcript...\n")

transcript = get_transcript(video_id)

print("Transcript:")
print(transcript[:2000])
