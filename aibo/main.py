import time
import argparse

import click
import whisper

from .config import get_config, ask_and_set_config
from .record import record_audio
from .transcribe import run_whisper
from .chat import run_chatgpt
from .text_to_speech import call_speaker

click.disable_unicode_literals_warning = True


class Aibo():
    def __init__(self, args) -> None:
        self.config = get_config()
        self.config["offline"] = args.offline

    def ask(self):
        start = time.time()
        call_speaker("How can I help you?")
        output_path = record_audio()

        text, output_path = run_whisper(output_path, self.config)

        text = run_chatgpt(text, output_path, self.config)

        call_speaker(text)

        end = time.time()
        print(end - start, "sec.")


def main():
    parser = argparse.ArgumentParser(description=None)

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        dest="verbosity",
        default=0,
        help="Set verbosity.",
    )

    def help(args):
        parser.print_help()

    parser.set_defaults(func=help)

    subparsers = parser.add_subparsers()
    sub = subparsers.add_parser("init", help="initialize aibo")
    sub.set_defaults(func=cli_init)

    sub = subparsers.add_parser("start", help="start aibo")
    sub.add_argument('-O', '--offline', action='store_true', help='run offline')
    sub.set_defaults(func=cli_start)

    args = parser.parse_args()
    args.func(args)


def cli_init(args):
    init()


def cli_start(args):
    my_aibo = Aibo(args)
    my_aibo.ask()


@click.command()
@click.argument("arg1")
def init(arg1):
    config = get_config()
    config = ask_and_set_config(config)

    MODEL = config["transcription_model"]
    MODEL, MODEL_SIZE = MODEL.split(":")
    _ = whisper.load_model(MODEL_SIZE)


if __name__ == "__main__":
    my_aibo = Aibo()
    my_aibo.ask()
