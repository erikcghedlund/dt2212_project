import numpy as np
import sounddevice as sd

freq = 220
samplerate = int(4.41e4)
length = 4
volume = 1
slope = -6
partials = 30

def sawtooth_wave(freq, length, samplerate, partials, slope):
    x = np.linspace(0, length, samplerate * length)
    return sum([np.sin(x * (freq*i * 2 * np.pi)) * db_to_amp(slope * i) for i in range(partials)])

def db_to_amp(db):
    return 10**(db/20)


def main():
    wave = sawtooth_wave(freq, length, samplerate, partials, slope)
    sd.play(wave * volume, samplerate)
    sd.wait()


if __name__ == "__main__":
    main()
