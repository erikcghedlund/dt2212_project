from bs4 import BeautifulSoup


class Song:

    def __init__(self, file):

        tonenames = (("C", ), ("C#", "Db"), ("D",), ("D#", "Eb"), ("E",), ("F",), ("F#", "Gb"), ("G",), ("G#", "Ab"), ("A",), ("A#", "Bb"), ("B",))

        self.__tone_to_midi_map = {
                "A0": 21,
                "A#0": 22,
                "Bb0": 22,
                "B0": 23
                }

        for i in range(24, 128):
            for t in tonenames[i % len(tonenames)]:
                self.__tone_to_midi_map["".join((t, str((i-24) // len(tonenames) + 1)))] = i

        if file[-len("musicxml"):] == "musicxml":
            self.__init_musicxml__(file)
        else:
            raise Exception()

    def __init_musicxml__(self, file):

        def strip_tags(val):  # This is not very smart and most likely a improper way to do this, but it does work
            if val is None:
                return None
            rval = str(val)
            return rval[rval.find(">")+1:rval.rfind("<")]

        self.notes = []
        with open(file, "r") as f:
            data = BeautifulSoup(f.read(), "xml")
            self.tempo = int(strip_tags(data.find("per-minute")))
            for note in data.find_all("note"):
                ttype = 2**-["whole", "half", "quarter", "eighth", "16th", "32th", "64th"].index(strip_tags(note.type)) if note.type is not None else None
                tstep = strip_tags(note.step)
                toctave = strip_tags(note.octave)
                tnote = self.__tone_to_midi_map["{}{}".format(tstep, toctave)] if None not in (tstep, toctave) else None
                self.notes.append((tnote, ttype))


if __name__ == "__main__":
    song = Song("Pokémon_Theme-Altsaxofon.musicxml")

    print("tempo={}".format(song.tempo))
    print("\n".join(map(str, song.notes)))
