# Concierge

The project aims to create an AI concierge that can run offline.

# Features

- You can choose your favorite AI model as your concierge.
- You don't need to worry about security and privacy.
- You and the concierge can communicate by voice.

# Installation

## With pip

This repository is tested on Python 3.8+ and PyTorch 1.13.1+.

You should install Concierge in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

First, create a virtual environment with the version of Python you're going to use and activate it.

Then, you will need to install PyTorch.
Please refer to [PyTorch installation page](https://pytorch.org/get-started/locally/#start-locally) regarding the specific installation command for your platform.

When one of those backends has been installed, Concierge can be installed using pip as follows:

```bash
pip install concierge
```

# Usage

First, configure the model you want to use, API, and API key. You can also set the parameters required for online execution at this point.

```bash
concierge init
```

Start concierge and start conversation. Your conversation history is stored in the history directory.

Offline execution is performed by appending "--offline" after this command.

```bash
concierge start
```
