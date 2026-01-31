import sys
from faster_whisper import WhisperModel

if len(sys.argv) != 3:
    print("Usage: transcribe.py <input_audio_or_video> <output_text_file>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

model = WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16",
    download_root="./model_cache"
)

segments, info = model.transcribe(
    input_path,

    # decoding
    beam_size=5,
    language="en",

    # VAD
    vad_filter=True,
    vad_parameters=dict(
        min_silence_duration_ms=500
    )
)

with open(output_path, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(
            f"[{segment.start:.2f} → {segment.end:.2f}] "
            f"{segment.text.strip()}\n"
        )

print(f"Transcription complete → {output_path}")
