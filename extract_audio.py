"""
    Extract the audio from a video given the path and create an audio file in the audio folder with the same prefix as video file.
"""

from moviepy.editor import VideoFileClip
import os
import subprocess

# Create output path with the same name as input with differnet extension
def generate_output_path(input_path: str, output_folder: str) -> str:
    """
    Generates an audio output path from the given video path.

    Parameters:
    input_path (str): Path to the input video file.
    output_folder (str): Folder to save the audio file.

    Returns:
    str: Path to the audio output file with .wav extension.
    """
    # Extract the file name
    file_name=os.path.basename(input_path)
    # Extract filename without extension
    base_name = os.path.splitext(file_name)[0]  # function generates a tuple with name and extension

    # Construct audio file path
    output_path = os.path.join(output_folder, f"{base_name}.wav")
    return output_path

# extract audio from the video file given in the path

def extract_audio(video_path):
    """
    Extracts audio from a video file and saves it as a WAV file.

    Parameters:
    video_path (str): Path to the input video file.
    output_audio_path (str): Path to save the extracted audio file.
    """
    try:
        video = VideoFileClip(video_path)
        output_audio_path = generate_output_path(video_path,"audio")   # Path where audio will be stored

        # Check if audio already exists
        if os.path.exists(output_audio_path):
            print(f"⚠️ Audio file already exists: {output_audio_path}")
        else:
            audio = video.audio   # extract the audio from the video
            if audio:
                # Save the audio in the specified path
                audio.write_audiofile(
                output_audio_path,
                codec="pcm_s16le",
                fps=16000  # Sample rate 16 kHz (required by Whisper)
                )
                print(f"✅ Audio extracted and saved to {output_audio_path}")
            else:
                print(f"[!] No audio track found in {video_path}")
    except Exception as e:
        print(f"[!] Error extracting audio from {video_path}: {e}")


'''def extract_audio(video_path):
    """
    Extracts audio from a video file and saves it as a WAV file using FFmpeg.

    Parameters:
    video_path (str): Path to the input video file.
    """
    try:
        output_audio_path = generate_output_path(video_path, "audio")
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)

        # Check if audio already exists
        if os.path.exists(output_audio_path):
            print(f"⚠️ Audio file already exists: {output_audio_path}")
            return

        # Use FFmpeg to extract audio
        cmd = [
            "ffmpeg",
            "-i", video_path,
            "-vn",  # No video
            "-acodec", "pcm_s16le",  # PCM signed 16-bit little-endian
            "-ar", "16000",  # Sample rate 16 kHz (required by Whisper)
            "-ac", "1",  # Mono
            output_audio_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Audio extracted and saved to {output_audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error extracting audio from {video_path}: {e.stderr}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")'''

# main function 
if __name__ == "__main__":
    video_file = "video/SQL.mp4"

    extract_audio(video_file)
