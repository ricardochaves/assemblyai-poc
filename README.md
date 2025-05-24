# Assemblyai POC

## Overview

This project demonstrates the use of AssemblyAI's transcription API to process audio files and generate speaker-labeled transcriptions.

## Environment Variables

The `.env` file contains the following configuration options:

- `ASSEMBLYAI_API_KEY`: Your AssemblyAI API key for authentication.
- `AUDIO_FILE`: Path to the audio file to be transcribed.
- `TRANSCRIPT_FILE`: Path where the generated transcription will be saved.

Ensure you create a `.env` file in the root directory and populate it with the required values before running the application.

## Functionality of `main.py`

The `main.py` file is the core of the application. It performs the following tasks:

1. **API Key Configuration**: Reads the API key from the `.env` file and configures the AssemblyAI client.
2. **Audio File Transcription**: Sends the specified audio file to the AssemblyAI API for transcription with speaker labeling and language settings.
3. **Output Generation**: Saves the transcription to the specified file and prints the speaker-labeled text to the console.

## Running with Docker Compose

To run the application using Docker Compose, follow these steps:

1. Ensure you have a `.env` file in the root directory with the [required environment variables](#environment-variables).
2. Build and start the containers:
   ```bash
   docker-compose up
   ```
3. Access the application logs in the terminal to view the transcription process.

To stop the containers, use:
```bash
docker-compose down
```
