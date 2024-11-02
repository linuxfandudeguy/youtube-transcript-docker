import sys
from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL

def get_video_id(url):
    return url.split("v=")[1].split("&")[0] if "v=" in url else url.split("/")[-1]

def extract_transcript(video_url):
    video_id = get_video_id(video_url)
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return "\n".join([f"{item['text']}" for item in transcript])
    except Exception as e:
        return f"Could not retrieve transcript: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_transcript.py <YouTube_URL>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    transcript = extract_transcript(video_url)
    
    print("Transcript:\n")
    print(transcript)
