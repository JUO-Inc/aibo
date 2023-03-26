import json

import click

with open(".config.json", "r") as f:
    API_KEY = json.load(f)["api_key"]


def ask_api_key(default):
    return click.prompt(
        text="Type in your api key",
        type=str,
        default=default
    )


def ask_transcribe_api_url(default):
    return click.prompt(
        text="Type in your transcribe API URL",
        type=str,
        default=default
    )


def ask_chat_api_url(default):
    return click.prompt(
        text="Type in your chat API URL",
        type=str,
        default=default
    )
