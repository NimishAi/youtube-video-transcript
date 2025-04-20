import streamlit as st
from transcript import get_youtube_transcript
import re
from summarize import summarize_text
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_language(video_id):
    try:
        # Fetch transcript metadata
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        # Return the language of the first available transcript
        transcripts = list(transcript_list)
        first_transcript = transcripts[0]

        return first_transcript.language_code
    except Exception as e:
        raise ValueError(f"Could not determine video language: {e}")

def extract_video_id(youtube_url):
    # Regular expression to extract the video ID
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", youtube_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

# Streamlit app
st.title("YouTube Video Transcript")

# Create a form
with st.form("youtube_form"):
    youtube_url = st.text_input("Enter YouTube URL:")
    submit_button = st.form_submit_button("Get Summary")

# Handle form submission
if submit_button:
    if youtube_url:
        try:
             # Extract video ID and fetch transcript
            video_id = extract_video_id(youtube_url)
            language = get_video_language(video_id)
            transcript = get_youtube_transcript(video_id, language)
            st.text_area("Summary", summarize_text(transcript), height=100)
            st.text_area("Transcript", transcript, height=500)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a YouTube URL.")

       