import json
import click
import os
import time
import sys

import whisper

from .config import get_config, ask_and_set_config
from .record import record_audio
from .transcribe import run_whisper
from .chat import run_chatgpt
from .text_to_speech import call_speaker

click.disable_unicode_literals_warning = True


class Concierge():
    def __init__(self) -> None:
        self.config = get_config()
        self.config["offline"] = "offline" == sys.argv[1]

    def ask(self):
        start = time.time()
        call_speaker("How can I help you?")
        output_path = record_audio()
        mid1 = time.time()
        text, output_path = run_whisper(output_path, self.config)
        mid2 = time.time()
        text = run_chatgpt(text, output_path, self.config)
        call_speaker(text)
        end = time.time()
        print(mid1 - start, mid2 - start, end - start)


def main():
    my_concierge = Concierge()
    my_concierge.ask()


@click.command()
def init():
    config = get_config()
    ask_and_set_config(config)

    MODEL = config["transcription_model"]
    MODEL, MODEL_SIZE = MODEL.split(":")
    _ = whisper.load_model(MODEL_SIZE)


if __name__ == "__main__":
    my_concierge = Concierge()
    my_concierge.ask()
    # record_audio()
