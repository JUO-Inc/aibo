import os
import requests
import warnings


def run_chatgpt(path, output_path, config):
    if config["offline"]:
        result = run_local_chatgpt(path, output_path, config)
    else:
        result = call_chatgpt(path, output_path, config)

    return result


def run_local_chatgpt(text, output_path, config):
    # <TODO> run ChatGPT offline
    warnings.warn("ChatGPT running offline is not yet implemented. So, We use ChatGPT API for now.")
    result = call_chatgpt(text, output_path, config)
    return result


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
    # print(result)
    result = result["choices"][0]["message"]["content"]
    print(result)
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
