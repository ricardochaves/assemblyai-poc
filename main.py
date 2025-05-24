import assemblyai as aai
import os

aai.settings.api_key = os.environ["ASSEMBLYAI_API_KEY"]

audio_file = os.environ["AUDIO_FILE"]
output_path = os.environ["TRANSCRIPT_FILE"]

config = aai.TranscriptionConfig(speaker_labels=True, language_code="pt")

transcript = aai.Transcriber().transcribe(audio_file, config)

with open(output_path, "w", encoding="utf-8") as f:
    for utterance in transcript.utterances:
        line = f"Speaker {utterance.speaker}: {utterance.text}\n"
        print(line, end="")
        f.write(line)

print(f"\n✅ Transcript saved in '{output_path}'")
