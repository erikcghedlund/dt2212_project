# Project Specification

## Speech synthesis of lyric sheets

### Introduction

### Problem

The problem of the MVP of the project consists of two parts. One; read the English lyrics and translate the lyrics to phonetics. Secondly, synthesize these phonetics and map them to the melody.

### Implementation


#### Tables of objects in simulation and their characteristics

##### Lyric parsing

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|

=======
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
>>>>>>> master

##### Speech synthesis

| Characteristic | Priority      | Complexity |
|:--------------:|:-------------:|:----------:|


##### Melody playback

| Characteristic | Depends on | Priority      | Complexity |
|:--------------:|:----------:|:-------------:|:----------:|
| The program should be able to map each vowel into a separate tone | # Lyric parsing #1 #2 | High | Low |
| The program should be able to transition in-between tones in a natural sounding way | Melody playback #1 | High | Medium |
| The program should be able to alter the tempo and melody sung | Melody playback #1 | Medium | Medium |
| The program may be able to pronounce the consonants of the phonetic words | Melody playback #1, # Lyric parsing #1 | Low | High |

#### User interface



### References
Python program that utilizes the Carnegie-Mellon University Pronouncing Dictionary to convert English text into the International Phonetic Alphabet.: https://pypi.org/project/eng-to-ipa/

### Risks

| Risk | Counter-actions |
|:--------------:|:-------------:|
| TODO | TODO |
