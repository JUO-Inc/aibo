import os
import requests
import json

from .config import API_KEY


def run_chatgpt(text, output_path):
    # <TODO> run GPT offline

    add_result(output_path, text)
    return text


def call_chatgpt(text, output_path, model="gpt-3.5-turbo"):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }

    json_data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": text,
            },
        ],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=json_data)

    result = response.json()
    print(result)
    result = result["choices"][0]["message"]["content"]
    add_result(output_path, result)
    return result


def add_result(output_path, result):
    dirname = os.path.dirname(output_path)
    text_path = os.path.join(dirname, "output.txt")
    with open(text_path, mode='a') as f:
        f.write("\n\n" + result)


if __name__ == "__main__":
    text = call_chatgpt("hello")
    print(text)
