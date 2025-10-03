"""
1. Extract audio from video (if not already extracted)
2. Transcribe the audio using Whisper
3. Convert transcription into .srt file with timestamps
"""

import os
from datetime import timedelta

import whisper
import srt

from extract_audio import generate_output_path, extract_audio  # fixed function name

# ---------------------------
# Transcription
# ---------------------------
def transcribe_audio(audio_path: str,model="base") -> dict:
    """
    Transcribe the audio file using Whisper.

    Parameters:
        audio_path (str): Path to the input audio file.

    Returns:
        dict: Transcription result containing text and segments.
    """
    print(f"Using the {model} whisper model.")
    model = whisper.load_model(model)  # load the whisper model: base or medium
    #result = model.transcribe(audio_path)
    result = model.transcribe(audio_path, task="translate")

    return result

# ---------------------------
# Convert transcription to SRT
# ---------------------------
def convert_to_srt(transcription: dict) -> str:
    """
    Convert Whisper transcription to SRT formatted text.

    Parameters:
        transcription (dict): Whisper transcription result with 'segments'.

    Returns:
        str: SRT formatted subtitles.
    """
    subtitles = []
    for i, seg in enumerate(transcription["segments"]):
        subtitle = srt.Subtitle(
            index=i + 1,
            start=timedelta(seconds=seg['start']),
            end=timedelta(seconds=seg['end']),
            content=seg['text'].strip()
        )
        subtitles.append(subtitle)
    return srt.compose(subtitles)

# ---------------------------
# Main function to generate SRT
# ---------------------------
def generate_srt_from_video(video_path: str,model="base"):
    """
    Generate a .srt file for a video.

    Parameters:
        video_path (str): Path to the input video file.
    """
    # Generate paths
    audio_path = generate_output_path(video_path, "audio")
    srt_path = generate_output_path(video_path, "caption").replace(".wav", ".srt")
    # check whether srt file exists or not
    if not os.path.exists(srt_path):
        # Create folders if not exist
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        os.makedirs(os.path.dirname(srt_path), exist_ok=True)

        # Extract audio and store it if it does not exist
        extract_audio(video_path)

        # Transcribe audio
        transcription = transcribe_audio(audio_path,model)

        # Convert to SRT and save
        srt_content = convert_to_srt(transcription)
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(srt_content)

        print(f"✅ SRT file generated and saved to {srt_path}")
    else:
        print(f"⚠️ Subtitle file already exists: {srt_path}")


if __name__ == "__main__":
    #video_path = "C:/Users/lenov/Videos/VideoProc Converter AI/Vizura/Python for ML/4_Pandas in Python for ML and Data Science_ A comprehensive introduction for beginners [Lecture 33].mp4"
    generate_srt_from_video(video_path,model = "base")
