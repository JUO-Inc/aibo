import json
import os
import requests

import whisper


def run_whisper(path, config):
    if config["offline"]:
        text, output_path = run_local_whisper(path, config)
    else:
        text, output_path = call_whisper(path, config)

    return text, output_path


def run_local_whisper(path, config, language="en"):
    print("Transcribing...")
    MODEL = config["transcription_model"]
    MODEL, MODEL_SIZE = MODEL.split(":")
    model = whisper.load_model(MODEL_SIZE)
    result = model.transcribe(path, language=language)
    print("Done.")
    print(result)
    if result["text"]:
        text = result["text"]
    else:
        text = "No Result"
    output_path = write_result(path, text)
    return text, output_path


def call_whisper(path, config):
    API_KEY = config["api_key"]
    URL = config["transcription_api_url"]
    MODEL = config["transcription_model"]
    MODEL, MODEL_SIZE = MODEL.split(":")

    headers = {"Authorization": "Bearer " + API_KEY}

    file = {
        "model": (None, MODEL),
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
