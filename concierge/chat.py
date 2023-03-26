import os
import requests


def run_chatgpt(text, output_path, config):
    # <TODO> run GPT offline

    add_result(output_path, text)
    return text


def call_chatgpt(text, output_path, config):
    API_KEY = config["api_key"]
    URL = config["chat_api_url"]
    MODEL = config["chat_model"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }

    json_data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": text,
            },
        ],
    }

    response = requests.post(
        URL,
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
