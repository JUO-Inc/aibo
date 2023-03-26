import json
import click
import os
import time

import whisper

from .config import CONFIG_PATH, get_config, ask_and_set_config
from .record import record_audio
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
        text = call_chatgpt(text, output_path)
        call_speaker(text)
        end = time.time()
        print(mid1 - start, mid2 - start, end - start)


def main():
    my_concierge = Concierge()
    my_concierge.ask()


@click.command()
def init():
    config = get_config()
    config = ask_and_set_config(config)

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)


if __name__ == "__main__":
    my_concierge = Concierge()
    my_concierge.ask()
    # record_audio()
