<h1 align="center">
   🔈Aibo
</h1>
<h3 align="center">
    <p>Offline Smart Speaker Engine Powered by ChatGPT</p>
</h3>

https://user-images.githubusercontent.com/62988216/228871916-f8311a31-be59-4855-b7d9-873e3f9adc10.mov

# Features

- Voice Prompting: You and Aibo can communicate by voice.
- Security and Privacy: You don't need to worry about security and privacy.
- Models: You can choose your favorite AI model as your aibo.

# Installation

## With pip

This repository is tested on Python 3.8+, PyTorch 1.13.1+ and MacOS 11.5.2+.

You should install aibo in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

First, create a virtual environment with the version of Python you're going to use and activate it.

Then, you will need to install PyTorch.
Please refer to [PyTorch installation page](https://pytorch.org/get-started/locally/#start-locally) regarding the specific installation command for your platform.

When one of those backends has been installed, aibo can be installed using pip as follows:

```bash
pip install aibo
```

# Usage

First, configure the model you want to use, API, and API key. You can also set the parameters required for online execution at this point.

```bash
aibo init
```

Start aibo and start conversation in English. Your conversation history is stored in the history directory.

Offline execution is performed by appending "--offline" after this command.

```bash
aibo start
```

# Models

We support the following APIs for online/offline execution.

| model                  | online | offline |
| :--------------------- | :----: | :-----: |
| ChatGPT(gpt-3.5-turbo) |  ⭕️   |   ❌    |
| Whisper                |  ⭕️   |   ⭕️   |
