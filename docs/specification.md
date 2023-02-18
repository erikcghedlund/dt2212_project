# Project Specification

## Speech synthesis of lyric sheets

### Introduction

### Problem

The problem of the MVP of the project consists of two parts. One; read the english lyrics and translate the lyrics to phonetics. Secondly, synthesize these phonetics and map them to the melody.

### Implementation




#### Tables of objects in simulation and their characteristics

##### Lyric parsing

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|
| The program should be able to parse english text into phonetic text | High | Easy |

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

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|
| TODO    | TODO | TODO |

#### User interface

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|
| Interface for parsing the English text into phoenetic text with a [convert] button | Medium High | Easy |
| Interface for changing every musical parameters | Medium High | Easy |


### References
Python program that utilizes the Carnegie-Mellon University Pronouncing Dictionary to convert English text into the International Phonetic Alphabet.: https://pypi.org/project/eng-to-ipa/

### Risks

| Risk | Counter-actions |
|:--------------:|:-------------:|
| TODO | TODO |
