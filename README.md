# dt2212_project

## What is this?

This is a program for parsing lyrics and score files and then singing them with the help of formant synthesis. Currently only
raw text files are supported for lyric sheets and only musicxml files for scores.

This program was developed for the course DT2212 Music Acoustics at KTH Royal Institute of Technology.

## Dependencies

This program requires `Python3.10`.

It also requires some third party modules that can be install with pip using the command

```bash
pip install -r ./requirements.txt
```

## Running the program

After installing the dependencies, running the program should be as easy as

```bash
python src/main.py <score-file> <lyric-file>
```

Using the scores provided in the repo to test it:

```bash
python src/main.py scores/Pokémon_Theme-Tenor.musicxml scores/Pokémon_Theme.txt
```
