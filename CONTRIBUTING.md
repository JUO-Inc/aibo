# Contribute to Concierge

Everyone is welcome to contribute, and we value everybody's contribution. Code contributions are not the only way to help the community. Answering questions, helping others, and improving the documentation are also immensely valuable.

It also helps us if you spread the word! Reference the library in blog posts about the awesome projects it made possible, shout out on Twitter every time it has helped you, or simply ⭐️ the repository to say thank you.

To contribute to this project, please follow a ["fork and pull request"](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow. Please do not try to push directly to this repo unless you are maintainer.

## Contributing Guidelines

### GitHub Issues

Our [issues](https://github.com/JUO-Inc/concierge/issues) page is kept up to date
with bugs, improvements, and feature requests.

If you start working on an issue, please assign it to yourself.

If you are adding an issue, please try to keep it focused on a single modular bug/improvement/feature.
If the two issues are related, or blocking, please link them rather than keep them as one single one.

We will try to keep these issues as up to date as possible, though
with the rapid rate of develop in this field some may get out of date.
If you notice this happening, please just let us know.

### Getting Help

Although we try to have a developer setup to make it as easy as possible for others to contribute (see below)
it is possible that some pain point may arise around environment setup, linting, documentation, or other.
Should that occur, please contact a maintainer! Not only do we want to help get you unblocked,
but we also want to make sure that the process is smooth for future contributors.

In a similar vein, we do enforce certain linting, formatting, and documentation standards in the codebase.
If you are finding these difficult (or even just annoying) to work with,
feel free to contact a maintainer for help - we do not want these to get in the way of getting
good code into the codebase.

### Release process

As of now, Concierge has an ad hoc release process: releases are cut with high frequency via by
a developer and published to [PyPI](https://pypi.org/project/concierge/).

Concierge follows the [semver](https://semver.org/) versioning standard. However, as pre-1.0 software,
even patch releases may contain [non-backwards-compatible changes](https://semver.org/#spec-item-4).

## ✅Common Tasks

Type `make` for a list of common tasks.

### Code Formatting

Formatting for this project is done via a combination of [Black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/).

To run formatting for this project:

```bash
make format
```

### Linting

Linting for this project is done via a combination of [Black](https://black.readthedocs.io/en/stable/), [isort](https://pycqa.github.io/isort/), [flake8](https://flake8.pycqa.org/en/latest/), and [mypy](http://mypy-lang.org/).

To run linting for this project:

```bash
make lint
```

We recognize linting can be annoying - if you do not want to do it, please contact a project maintainer, and they can help you with it. We do not want this to be a blocker for good code getting contributed.

### Testing

Unit tests cover modular logic that does not require calls to outside APIs.

If you add new logic, please add a unit test.

Integration tests cover logic that requires making calls to outside APIs (often integration with other services).

## Documentation

### Contribute Documentation
