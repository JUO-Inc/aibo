import os
import datetime
import math
import wave

import audioop
import pyaudio


def record_audio():
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(os.path.join("history", now))
    CHUNK = 2**10
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    MAX_RECORD_SECONDS = 60
    MIN_RECORD_SECONDS = 2  # Minimum recording time in seconds
    output_path = os.path.join("history", now, "output.wav")
    THRESHOLD = 35  # Audio threshold in dB
    silent_frames = 0

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * MAX_RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

        # Calculate root mean square (RMS) volume of audio
        rms = audioop.rms(data, 2)
        db = 20 * math.log10(rms)
        # if i % 100 == 0:
        #     print(db, len(frames))

        if db < THRESHOLD:
            # If audio level falls below threshold, increment silent frames counter
            silent_frames += 1
        else:
            # If audio level is above threshold, reset silent frames counter
            silent_frames = 0

        if silent_frames > int(MIN_RECORD_SECONDS * RATE / CHUNK):
            # If there have been enough silent frames, stop recording
            break
    print("Done.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return output_path


if __name__ == "__main__":
    output_path = record_audio()
