import os
import json

import click

CONFIG_PATH = "config.json"


def get_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
    else:
        config = {
            "api_key": "YOUR KEY",
            "transcription_api_url": "https://api.openai.com/v1/audio/transcriptions",
            "transcription_model": "whisper-1:medium",
            "chat_api_url": "https://api.openai.com/v1/chat/completions",
            "chat_model": "gpt-3.5-turbo"
        }

    return config


def ask_and_set_config(config):
    api_key = ask_api_key(config["api_key"])
    transcription_api_url = ask_transcription_api_url(config["transcription_api_url"])
    transcription_model = ask_transcription_model(config["transcription_model"])
    chat_api_url = ask_chat_api_url(config["chat_api_url"])
    chat_model = ask_chat_model(config["chat_model"])

    config["api_key"] = api_key
    config["transcription_api_url"] = transcription_api_url
    config["transcription_model"] = transcription_model
    config["chat_api_url"] = chat_api_url
    config["chat_model"] = chat_model

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)


def ask_api_key(default):
    return click.prompt(
        text="Type in your api key",
        type=str,
        default=default
    )


def ask_transcription_api_url(default):
    return click.prompt(
        text="Type in your transcription API URL",
        type=str,
        default=default
    )


def ask_transcription_model(default):
    return click.prompt(
        text="Type in your transcription model",
        type=str,
        default=default
    )


def ask_chat_api_url(default):
    return click.prompt(
        text="Type in your chat API URL",
        type=str,
        default=default
    )


def ask_chat_model(default):
    return click.prompt(
        text="Type in your chat model",
        type=str,
        default=default
    )
