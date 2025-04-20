from youtube_transcript_api import YouTubeTranscriptApi

def extract_texts_from_transcript(transcript):
    texts = []
    for entry in transcript:
        if 'text' in entry:
            texts.append(entry['text'])
    return ' '.join(texts)

def get_youtube_transcript(video_id, language):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        # Format the transcript as plain text
        plain_text_transcript = extract_texts_from_transcript(transcript)
        return plain_text_transcript
    except Exception as e:
        return f"An error occurred: {e}"
