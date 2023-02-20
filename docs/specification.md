# Project Specification

## Speech synthesis of lyric sheets

### Introduction

### Problem

The problem of the MVP of the project consists of two parts. One; read the English lyrics and translate the lyrics to phonetics. Secondly, synthesize these phonetics and map them to the melody.

### Implementation

#### Specification of program parts

##### Lyric parsing

| Characteristic | Depends on | Priority      | Complexity |
|:--------------:|:----------:|:-------------:|:----------:|
| The program should be able to parse English text into phonetic text | N/A | High | Easy |
| The program should be able to filter out consonants | Lyric parsing #1 | High | Easy |
| The program should be able to split the lyrics into separate syllables | Lyric parsing #1 | High | Medium |
| The program should be able to read a external text file and parse it | Lyric parsing #1 | High | Easy |
| The program may be able to read a external pdf file for the lyrics | Lyric parsing #1 | Low | Easy |
| The program may be able to read a external a image file and interpret it for the lyrics | Lyric parsing #1 | Low | Easy |

##### Speech synthesis

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|
| The program should be able to identify the Frequency and Formant of every phonetic text | High | Easy |
| The program should be able to synthesis individual phonetic text| High | Easy |

##### Melody parsing

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|
| The program should be able to parse phonetic text into Melody | Medium | Medium |
| The program should be able to synthesis phonetic text with dynamic | Medium | Medium |


##### Melody playback

| Characteristic | Depends on | Priority      | Complexity |
|:--------------:|:----------:|:-------------:|:----------:|
| The program should be able to map each vowel into a separate tone | # Lyric parsing #1 #2 | High | Low |
| The program should be able to transition in-between tones in a natural sounding way | Melody playback #1 | High | Medium |
| The program should be able to alter the tempo and melody sung | Melody playback #1 | Medium | Medium |
| The program may be able to pronounce the consonants of the phonetic words | Melody playback #1, # Lyric parsing #1 | Low | High |

#### User interface

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|
| Interface for parsing the English text into phonetic text with a [convert] button | Medium High | Easy |
| Interface for changing every musical parameters | Medium High | Easy |



### References/Dependencies

- [Well used math-library Numpy that will be used to generate the waveforms](https://numpy.org/)

- [Library for generating sound from Numpy-arrays](https://python-sounddevice.readthedocs.io/en/0.4.5/index.html#)

- [Python program that utilizes the Carnegie-Mellon University Pronouncing Dictionary to convert English text into the International Phonetic Alphabet.](https://pypi.org/project/eng-to-ipa/)

- [Formants of the different phonetic vowels](https://corpus.eduhk.hk/english_pronunciation/index.php/2-2-formants-of-vowels/)

### Risks

| Risk | Counter-actions |
|:--------------:|:-------------:|
| TODO | TODO |
