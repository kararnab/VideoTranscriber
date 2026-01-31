# 🎙️ Local GPU Transcription with Faster-Whisper (Docker)

A fully local, GPU-accelerated transcription pipeline using **faster-whisper**, packaged in Docker so you don’t have to fight Python, CUDA, or dependency hell.

## ✨ Highlights
```
✅ Runs entirely on your machine (100% local & offline)
✅ GPU-accelerated (5–10× faster than CPU)
✅ Supports Whisper large-v3
✅ Dockerized (no Python / CUDA pain)
✅ Works great for long videos
```

## 🧠 Who Is This For?

This section helps people self-identify (very important for engagement):

- 📚 Students transcribing lectures
- 👨‍💻 Engineers watching system design talks
- 🎥 YouTubers & course creators
- 🔒 Anyone working with sensitive or private audio
- 🤖 People building LLM pipelines on top of transcripts

If you watch **long videos and take notes**, this saves hours.

## 🚀 What This Does

- Transcribes audio/video files using Whisper models
- Uses your NVIDIA GPU for fast inference
- Outputs clean, timestamped transcripts

## 🧩 Requirements
### Hardware
- NVIDIA GPU (tested with RTX series)
- ~12 GB VRAM recommended for large-v3

### Software
- Docker Desktop
- NVIDIA GPU Driver
- NVIDIA Container Toolkit

## 🛠️ Getting Started

### Build the Docker Image (Once)

```bash
docker build -t whisper-local -f docker/Dockerfile docker
```
This creates a reusable image with:

- Ubuntu 22.04
- CUDA runtime
- Python 3.11
- faster-whisper
- FFmpeg

### Run Transcription
#### Windows Cmd Prompt
```bash
docker run --rm --gpus all -v "%cd%\input:/input" -v "%cd%\output:/output" whisper-local transcribe.py /input/video.mp4 /output/video.txt
```
#### Windows Power shell
```bash
docker run --rm --gpus all -v "${PWD}\input:/input" -v "${PWD}\output:/output" -v "${PWD}\model_cache:/app/model_cache" whisper-local transcribe.py /input/video.mp4 /output/video.txt
```

#### Linux / macOS
```bash
docker run --rm --gpus all \
  -v "$(pwd)/input:/input" \
  -v "$(pwd)/output:/output" \
  whisper-local transcribe.py /input/video.mp4 /output/video.txt
```

After completion, you’ll find:
```
transcripts/video.txt
```
### Output Example
```
[00:00:03] In this video, we’re going to talk about distributed systems…
[00:02:41] A common mistake engineers make is assuming consistency…
[00:07:12] Let’s walk through a real-world architecture example…
```
Clean. Timestamped. Ready for:

- Search
- Notes
- Summaries
- LLM pipelines

## Troubleshoot

### Verify GPU usage
To confirm the container is using your GPU:
```bash
nvidia-smi
```
You should see activity during transcription.

## 🔒 Privacy & Offline Use

- Your audio/video never leaves your machine
- Models are downloaded once from Hugging Face
- After that, transcription works fully offline

You may see this warning on first run:
`Warning: You are sending unauthenticated requests to the HF Hub`

This is **normal** and **safe**.

## 🧠 Designed for Knowledge Pipelines

This project is the first stage of a larger workflow:
```
Local
├── Transcription (completed)
├── Transcript cleanup (remove fillers, noise)
└── Chunking

Cloud / LLM
├── Note extraction
├── Summaries
└── Insights
```
The goal is to evolve this into a knowledge extraction pipeline, not just a transcription script.

## 🚧 Project Status

### Current state
- Fully local, GPU-accelerated transcription using faster-whisper
- Dockerized setup (no Python / CUDA dependency issues)
- Works with any audio or video file
- Outputs clean, timestamped transcripts

What this project does today
- 🎧 Audio/Video → Text (fast, local, private)
- 📄 Produces transcripts suitable for downstream processing (notes, summaries, search)

### 🔮 Future Direction (Planned)

- Batch transcription for entire folders
- Markdown-formatted outputs
- Transcript chunking for long videos
- LLM-based note extraction and summarization
- Optional local vs cloud summarization workflows

The goal is to evolve this from a transcription tool into a knowledge extraction pipeline.

### Promt Engineering
You are a senior engineer.
Convert this transcript into:
1. Key ideas
2. Step-by-step explanation
3. Practical takeaways
4. Common mistakes or warnings
5. A short summary

[Your_Transcript_here]

## 🤝 Contributing

If this saved you time:

⭐ Star the repo

🧠 Share it with someone who watches long videos

🛠️ Open a PR or issue