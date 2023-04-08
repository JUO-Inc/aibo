import os
import requests
import warnings


def run_chatgpt(prompt: str, output_path: str, config: dict, chat_history: list):
    if config["offline"]:
        result = run_local_chatgpt(prompt, output_path, config, chat_history)
    else:
        result = call_chatgpt(prompt, output_path, config, chat_history)

    return result


def run_local_chatgpt(prompt: str, output_path: str, config: dict, chat_history: list):
    # <TODO> run ChatGPT offline
    warnings.warn("ChatGPT running offline is not yet implemented. So, We use ChatGPT API for now.")
    result = call_chatgpt(prompt, output_path, config, chat_history)
    return result


def call_chatgpt(prompt: str, output_path: str, config: dict, chat_history: list):
    API_KEY = config["api_key"]
    URL = config["chat_api_url"]
    MODEL = config["chat_model"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    if chat_history:
        messages = []
        for i, chat in enumerate(chat_history):
            if i % 2 == 0:
                messages.append({
                    "role": "user",
                    "content": chat,
                })
            else:
                messages.append({
                    "role": "assistant",
                    "content": chat,
                })
    else:
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]

    json_data = {
        "model": MODEL,
        "messages": messages
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


def add_result(output_path: str, result: str):
    dirname = os.path.dirname(output_path)
    text_path = os.path.join(dirname, "output.md")
    with open(text_path, mode='a') as f:
        f.write("\n\n" + result + "\n\n")


if __name__ == "__main__":
    text = call_chatgpt("hello")
    print(text)
