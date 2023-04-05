import pyttsx3


def call_speaker(text: str, config):
    engine = pyttsx3.init()
    change_voice(engine, config["language"], config["gender"])

    engine.say(text)
    engine.runAndWait()


def change_voice(engine, language="en_US", gender='F'):
    voices = engine.getProperty('voices')
    gender_interpreter = {"M": "VoiceGenderMale", "F": "VoiceGenderFemale"}
    _gender = gender_interpreter[gender]
    for voice in voices:
        if language in voice.languages and _gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    gender_dict = {"VoiceGenderMale": "M", "VoiceGenderFemale": "F"}
    options = []
    for voice in voices:
        options.append((voice.languages[0], gender_dict[voice.gender]))
    raise RuntimeError(
        "Language '{}' for gender '{}' not found. Available options are \n {}".format(
            language, gender, options))


if __name__ == "__main__":
    call_speaker("hello", {"language": "en_UK", "gender": "M"})
