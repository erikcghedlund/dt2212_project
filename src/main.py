import numpy as np
import sounddevice as sd
import eng_to_ipa as ipa
import sys
from copy import deepcopy

from cachetools import cached, LRUCache
from shelved_cache import PersistentCache

from song import Song

freq = 100
samplerate = int(3.2e4)
length = 5
volume = 0.01
slope = -2
partials = np.floor(samplerate/(2*freq))
transition_time = 0.3

vibrato_cents = 50
vibrato_len = 0.2

bandwidths = [25, 40, 60, 80, 100]
singers_formant = [2400, 2800]

cache_file = ".cache"
pc = PersistentCache(LRUCache, cache_file, maxsize=32)


def vibrato_wave(freq, length, amp, samplerate, vibrato_cents, vibrato_length):

    freq_dev = np.abs(freq - freq * 2 ** (vibrato_cents / 1200))
    x = np.linspace(0, length, int(samplerate * length))
    modulation_wave = np.sin(x * 2 * np.pi * vibrato_length**-1) * freq_dev
    phase_corrections = np.cumsum(np.multiply( x, np.concatenate(( np.zeros(1), 2 * np.pi * np.subtract(modulation_wave[:-1], modulation_wave[1:])))))
    lst = list(map(
                lambda xt, m, pc: np.sin(xt * 2 * np.pi * (freq + m) + pc) * amp,
                x,
                modulation_wave,
                phase_corrections
                ))
    return np.array(lst)


@cached(pc)
def sawtooth_wave(freq, length, samplerate, partials, slope):
    wave = np.zeros(int(samplerate * length))
    for i in np.arange(1, partials + 1):
        print("/".join(map(str, (i, partials))))
        vib_wave = vibrato_wave(freq * i, length, db_to_amp(slope * i), samplerate, vibrato_cents, vibrato_len)
        wave = np.add(wave, vib_wave)
    return wave


def transition_wave(end_wave, new_wave):
    l = min((int(transition_time * samplerate), len(end_wave), len(new_wave)))//2
    slope_fact = np.linspace(0, 1, l * 2)
    slope_up = np.multiply(np.concatenate((new_wave[-l:], new_wave[:l])), slope_fact)
    slope_down = np.multiply(np.concatenate((end_wave[-l:], end_wave[:l])), list(reversed(slope_fact)))
    transition_wave = slope_up + slope_down
    ret_wave = np.concatenate((end_wave[:-l], transition_wave, new_wave[l:]))
    return ret_wave

def db_to_amp(db):
    return 10**(db/20)


def joli_lowpass_formant_resonator(wave, t, formants, bandwidths):

    q_factors = np.array(formants) / np.array(bandwidths)

    betas  = list(map(lambda formant: formant * 2 * np.pi, formants))
    alphas = list(map(lambda beta, q_factor: beta * np.sqrt(1+1 / (4*q_factor**2)) * ((q_factor*2)**-1), betas, q_factors))
    a1s    = list(map(lambda alpha, beta: -2 * np.exp(-alpha*t) * np.cos(beta * t), alphas, betas))
    a2s    = list(map(lambda alpha: np.exp(-2*alpha*t), alphas))
    gs     = list(map(lambda a1, a2: 1 + a1 + a2, a1s, a2s))

    ret_wave = np.concatenate((np.zeros(2), wave[2:]))

    for g, a1, a2 in zip(gs, a1s, a2s):
        for i in range(2, len(ret_wave)):
            ret_wave[i] = ret_wave[i]*g - ret_wave[i-1]*a1 - ret_wave[i-2]*a2

    return ret_wave

def trans_eng_into_ipa(words):
    return ipa.convert(words)

def vowel_to_formant(vowel):
    vowel_formant_map = {
        "i" : [280, 2250, 2890],
        "ɪ" : [400, 1920, 2560],
        "e" : [405, 2080, 2720],
        "ɛ" : [550, 1770, 2490],
        "æ" : [690, 1660, 2490],
        "a" : [710, 1100, 2540],
        "ɔ" : [550, 880, 2540],
        "o" : [430, 980, 2480],
        "ʊ" : [450, 1030, 2380],
        "u" : [310, 870, 2250],
        "ʌ" : [680, 1310, 2710],
        }
    return vowel_formant_map[vowel]

def filterletter(letter):
    vowels_list = ["i","ɪ","e","ɛ","æ","a","ɔ","o","ʊ","u","ʌ"]
    return letter in vowels_list

def midinum_to_freq(midi):
    return 440 * 2 ** ((midi-69) / 12)


def sing_song(song: Song, vowels):

    waves = generate_sawtooth_sequence(song)
    len_vowels = len(vowels)
    filtered_wave = [joli_lowpass_formant_resonator(wave, samplerate**-1, sorted(singers_formant + vowel_to_formant(vowels[i%len_vowels])), bandwidths) for i, wave in enumerate(waves)]
    ret_wave = transition_wave(filtered_wave[0], filtered_wave[1])
    for fwave in filtered_wave[2:]:
        ret_wave = transition_wave(ret_wave, fwave)
    return ret_wave

def generate_sawtooth_sequence(song:Song):

    time_per_meas = song.tempo**-1 * 4 * 60

    def foo(note):
        match note:
            case (None, None):
                return np.zeros(0)
            case (None, _):
                return np.zeros(int(time_per_meas * note[1] * samplerate))
            case _:
                return sawtooth_wave(midinum_to_freq(note[0]), time_per_meas * note[1], samplerate, partials, slope)

    return map(foo, song.notes)


def main():
    wave = sawtooth_wave(freq, length, samplerate, partials, slope)
    with open(sys.argv[2]) as f:
        contents = f.read()
    ipa = trans_eng_into_ipa(contents)
    filtered_object = filter(filterletter, ipa)
    filtered_list = list(filtered_object)
    voice = sing_song(Song(sys.argv[1]), filtered_list)
    sd.play(voice * volume, samplerate)
    sd.wait()

if __name__ == "__main__":
    main()
