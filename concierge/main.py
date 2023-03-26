import json
import click
import os
import time

import whisper

from .config import ask_api_key, ask_chat_api_url, ask_transcribe_api_url
from .recording import record_audio
from .transcribe import run_whisper, call_whisper
from .chat import call_chatgpt, run_chatgpt
from .text_to_speech import call_speaker

click.disable_unicode_literals_warning = True


class Concierge():
    def __init__(self) -> None:
        _ = whisper.load_model("medium")

    def ask(self):
        start = time.time()
        call_speaker("How can I help you?")
        output_path = record_audio()
        mid1 = time.time()
        text, output_path = call_whisper(output_path)
        mid2 = time.time()
        text = run_chatgpt(text, output_path)
        call_speaker(text)
        end = time.time()
        print(mid1 - start, mid2 - start, end - start)


def main():
    my_concierge = Concierge()
    my_concierge.ask()


@click.command()
def init():
    config_path = ".config.json"
    with open(config_path, "r") as f:
        config = json.load(f)

    api_key = ask_api_key(config["api_key"])
    transcribe_api_url = ask_transcribe_api_url(config["transcribe_api_url"])
    chat_api_url = ask_chat_api_url(config["chat_api_url"])

    config["api_key"] = api_key
    config["transcribe_api_url"] = transcribe_api_url
    config["chat_api_url"] = chat_api_url

    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)


if __name__ == "__main__":
    my_concierge = Concierge()
    my_concierge.ask()
    # record_audio()
