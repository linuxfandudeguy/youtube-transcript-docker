# Use an Alpine image that already has Python installed
FROM python:3.9-alpine

# Install necessary Python libraries
RUN pip install --no-cache yt-dlp youtube-transcript-api

# Set up working directory
WORKDIR /app

# Copy the Python script into the container
COPY extract_transcript.py .

# Set entrypoint for the script
ENTRYPOINT ["python", "extract_transcript.py"]
