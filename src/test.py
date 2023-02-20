#!/bin/python3

import numpy as np
import sounddevice as sd

freq = 440
samplerate = int(4.41e4)
length = 4
volume = 0.3


def main():
    x = np.linspace(0, length, samplerate * length)
    wave = np.sin(x * (freq * 2 * np.pi))
    sd.play(wave * volume, samplerate)
    sd.wait()


if __name__ == "__main__":
    main()
