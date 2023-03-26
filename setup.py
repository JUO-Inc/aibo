from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='concierge',
        version='0.0.1',
        packages=find_packages("concierge"),
        entry_points={
            'console_scripts': [
                'concierge init = concierge.main:init',
                'concierge start = concierge.main:main'
            ],
        },
        python_requires=">=3.8.0",
        install_requires=[
            "click",
            "pyttsx3",
            "pyaudio",
            "openai-whisper"
        ],
    )
