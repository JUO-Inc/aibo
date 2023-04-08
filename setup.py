from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='aibo',
        version='0.0.4',
        description="aibo: AI partner that can run offline",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        author="Aibo Community",
        author_email="koki.noda.contact@gmail.com",
        packages=find_packages(exclude=["tests*"]),
        entry_points={
            'console_scripts': [
                'aibo=aibo.main:main'
            ],
        },
        python_requires=">=3.7.0",
        install_requires=[
            "click",
            "pyttsx3",
            "pyaudio",
            "openai-whisper"
        ],
        url="https://github.com/JUO-Inc/aibo",
        keywords="LLM language model offline NLP speech deep learning transformer pytorch tensorflow GPT smart speaker",
        license="MIT",
    )
