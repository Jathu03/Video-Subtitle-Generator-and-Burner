# Video Subtitle Generator and Burner

This project provides a set of Python scripts to automatically generate subtitles for videos and burn them into the video files. The workflow involves extracting audio from videos, transcribing the audio using OpenAI's Whisper model, converting the transcription to SRT format, and finally embedding the subtitles into the video using FFmpeg.

## Features

- **Audio Extraction**: Extract audio from video files (MP4, etc.) and save as WAV format.
- **Automatic Transcription**: Use Whisper AI to transcribe audio into text with timestamps.
- **SRT Generation**: Convert transcription results into standard SRT subtitle files.
- **Subtitle Burning**: Embed subtitles directly into video files using FFmpeg.
- **Efficient Processing**: Skip processing if output files (audio or SRT) already exist.
- **Model Selection**: Choose Whisper model size (e.g., "base", "small", "medium") for transcription quality vs. speed trade-off.

## Requirements

- Python 3.7+
- FFmpeg (for subtitle burning)
- Required Python packages:
  - `whisper` (OpenAI Whisper)
  - `moviepy` (for audio extraction)
  - `srt` (for SRT file handling)

## Installation

1. Clone or download this repository.

2. Install Python dependencies:

   ```bash
   pip install openai-whisper moviepy srt
   ```

3. Download and install FFmpeg:
   - Download from [FFmpeg official site](https://ffmpeg.org/download.html)
   - Add FFmpeg to your system PATH, or provide the full path when using `burn_subtitles.py`

## Usage

### 1. Audio Extraction (`extract_audio.py`)

Extract audio from a video file:

```python
from extract_audio import extract_audio

video_path = "path/to/your/video.mp4"
extract_audio(video_path)
```

This will create a WAV file in the `audio/` folder with the same base name as the video.

### 2. SRT Generation (`srt_generator.py`)

Generate subtitles from a video (extracts audio if needed and transcribes):

```python
from srt_generator import generate_srt_from_video

video_path = "path/to/your/video.mp4"
generate_srt_from_video(video_path, model="base")  # Options: "base", "small", "medium", etc.
```

This will create an SRT file in the `caption/` folder.

### 3. Burn Subtitles (`burn_subtitles.py`)

Burn subtitles into a video (generates SRT if needed):

```python
from burn_subtitles import burn_subtitles

video_path = "path/to/your/video.mp4"
ffmpeg_path = "path/to/ffmpeg.exe"  # Or just "ffmpeg" if in PATH
burn_subtitles(video_path, ffmpeg_path, model="base")
```

This will create a new video file with burned-in subtitles in the `output/` folder.

## Folder Structure

After running the scripts, your directory will have:

```
project/
├── audio/          # Extracted audio files (.wav)
├── caption/        # Generated subtitle files (.srt)
├── output/         # Videos with burned subtitles (.mp4)
├── extract_audio.py
├── srt_generator.py
├── burn_subtitles.py
└── README.md
```

## Command Line Usage

You can also run the scripts directly:

- Extract audio: `python extract_audio.py` (edit the video path inside)
- Generate SRT: `python srt_generator.py` (edit the video path inside)
- Burn subtitles: `python burn_subtitles.py` (edit paths inside)

## Notes

- The scripts use translation mode (`task="translate"`) in Whisper, which translates to English.
- Audio is extracted at 16kHz mono for optimal Whisper performance.
- SRT files include timestamps and subtitle text.
- FFmpeg path must be provided for subtitle burning on Windows.
- Processing can be time-intensive for longer videos; choose appropriate Whisper model size.

## Troubleshooting

- Ensure FFmpeg is installed and accessible.
- Check that input video files exist and are valid.
- For large videos, consider splitting them or using a more powerful machine.
- If transcription quality is poor, try a larger Whisper model (e.g., "medium").

## License

This project is open-source. Please check individual library licenses for Whisper, moviepy, and srt.
