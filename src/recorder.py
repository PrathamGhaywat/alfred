import sounddevice as sd
import wavio

def record(file_name: str):
    duration = 5
    sample_rate = 44100
    print("recording")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    wavio.write(file_name, audio, sample_rate, sampwidth=2)
    print(f"done: {file_name}")


record("C:/Users/Prath/Programming/alfred/testing_assets/test.wav")