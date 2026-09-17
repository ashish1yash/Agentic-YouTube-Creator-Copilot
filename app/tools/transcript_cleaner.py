import re


class TranscriptCleaner:

    def clean(self, transcript: str) -> str:
        if not transcript:
            return ""

        # Remove bracketed transcript markers
        # Example: [Music], [Applause], [♪♪♪]
        transcript = re.sub(r"\[.*?\]", "", transcript)

        # Remove music-note symbols
        transcript = transcript.replace("♪", "")

        # Fix common cases where transcript formatting
        # accidentally joins words
        transcript = re.sub(r"([a-z])([A-Z])", r"\1 \2", transcript)

        # Normalize whitespace
        transcript = re.sub(r"\s+", " ", transcript)

        # Remove leading/trailing whitespace
        transcript = transcript.strip()

        return transcript
