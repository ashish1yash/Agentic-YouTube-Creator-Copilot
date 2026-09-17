from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)

    # Normal YouTube URL
    if parsed_url.hostname in {"www.youtube.com", "youtube.com"}:
        video_id = parse_qs(parsed_url.query).get("v")

        if video_id:
            return video_id[0]

    # Short YouTube URL
    if parsed_url.hostname == "youtu.be":
        video_id = parsed_url.path.strip("/")

        if video_id:
            return video_id

    raise ValueError("Invalid YouTube URL")


def get_transcript(video_id: str) -> str:
    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join(snippet.text for snippet in transcript)

    return text
