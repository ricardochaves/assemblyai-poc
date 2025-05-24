# Assemblyai POC

## How to use this image

### Docker compose

```text
root/
├── audio/
│   └── audio.m4a
├── .env
├── docker-compose.yml
└── after_run_your_txt_file_will_be_here.txt
```
```yml
services:
  app:
    image: ricardobchaves6/assemblyai-poc:latest
    container_name: assemblyai
    env_file: .env
    volumes:
      - .:/app 
```
`.env` file should contain the following variables:
```env
ASSEMBLYAI_API_KEY="YOUR_ASSEMBLYAI_API_KEY"
AUDIO_FILE="./audio/audio.m4a"
TRANSCRIPT_FILE="./transcript.txt"
```
Run compose
```bash
docker compose up
```

### Docker run

Create a `.env` file in the current directory with the following content:
```env
ASSEMBLYAI_API_KEY="YOUR_ASSEMBLYAI_API_KEY"
AUDIO_FILE="./audio/audio.m4a"
TRANSCRIPT_FILE="./transcript.txt"
```
```env

```bash
docker run --rm \
  --name assemblyai \
  --env-file .env \
  -v "$(pwd)":/app \
  image123:latest
```