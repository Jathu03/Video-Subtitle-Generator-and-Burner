import subprocess
import os
import sys
from extract_audio import generate_output_path
from srt_generator import generate_srt_from_video


def burn_subtitles(video_path: str, ffmpeg_path: str, subtitle_folder: str = "caption", output_folder: str = "output",model:str = "base") -> None:
    """
    Burn subtitles into a video using FFmpeg.

    Parameters:
        video_path (str): Path to input video file
        ffmpeg_path (str): Path to ffmpeg executable
        subtitle_folder (str): Folder to save/read subtitle (.srt) file (default: "caption")
        output_folder (str): Folder to save output video file (default: "output")
    """
    # Generate paths
    subtitle_path = generate_output_path(video_path, subtitle_folder).replace(".wav", ".srt")
    output_path = generate_output_path(video_path, output_folder).replace(".wav", "_burned.mp4")

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(subtitle_folder, exist_ok=True)
    
    generate_srt_from_video(video_path,model)

    # Convert paths to absolute
    video_path = os.path.abspath(video_path)
    subtitle_path = os.path.abspath(subtitle_path)
    output_path = os.path.abspath(output_path)

    # Handle Windows subtitle path escaping
    subtitle_path_escaped = subtitle_path.replace("\\", "\\\\").replace(":", "\\:")

    command = [
        ffmpeg_path,
        "-i", video_path,
        "-vf", f"subtitles='{subtitle_path_escaped}'",
        "-c:a", "copy",
        output_path
    ]

    print("Running command:")
    print(" ".join(command))

    try:
        subprocess.run(command, check=True)
        print(f"✅ Subtitles burned successfully: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred while burning subtitles: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    video_path = "video/Steal Her Breath 2024.mp4"
    ffmpeg_path = r"C:\ffmpeg-2025-09-10-git-c1dc2e2b7c-essentials_build\bin\ffmpeg.exe"

    # burn the subtitles    

    burn_subtitles(video_path, ffmpeg_path,model = "small")