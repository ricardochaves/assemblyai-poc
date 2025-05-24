# Assemblyai POC

## How to use this image

### Docker compose

```text
root/
├── audio/
│   └── audio.m4a
├── .env
├── docker-compose.yml
└── result/
    └── after_run_your_txt_file_will_be_here.txt
```
```yml
services:
  app:
    image: ricardobchaves6/assemblyai-poc:latest
    container_name: assemblyai
    env_file: .env
    volumes:
      - ./audio:/app/audio
      - ./result:/app/result
```
`.env` file should contain the following variables:
```env
ASSEMBLYAI_API_KEY="YOUR_ASSEMBLYAI_API_KEY"
AUDIO_FILE="./audio/audio.m4a"
TRANSCRIPT_FILE="./result/transcript.txt"
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
TRANSCRIPT_FILE="./result/transcript.txt"
```
```env

```bash
docker run --rm \
  --name assemblyai \
  --env-file .env \
  -v "$(pwd)"/audio:/app/audio \
  -v "$(pwd)"/result:/app/result \
  image123:latest
```