import json
import os
import requests

import whisper

from .config import API_KEY


def run_whisper(path, language="en"):
    print("Transcribing...")
    model = whisper.load_model("medium")
    result = model.transcribe(path, language=language)
    print("Done.")
    print(result)
    if result["text"]:
        text = result["text"]
    else:
        text = "No Result"
    output_path = write_result(path, text)
    return text, output_path


def call_whisper(path):
    URL = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": "Bearer " + API_KEY}

    file = {
        "model": (None, "whisper-1"),
        "file": open(path, "rb"),
    }

    response = requests.post(
        URL,
        headers=headers,
        files=file
    )

    result = response.json()
    print(result)
    if result["text"]:
        text = result["text"]
    else:
        text = "No Result"
    output_path = write_result(path, text)
    return text, output_path


def write_result(path, text):
    oldpath = os.path.dirname(path)
    newpath = oldpath + "-" + text[:20]
    os.makedirs(newpath)
    os.rename(oldpath, newpath)
    output_path = os.path.join(newpath, "output.txt")
    with open(output_path, "w") as f:
        f.write(text)
    return output_path


if __name__ == "__main__":
    text = call_whisper("output.wav")
    print(text)
