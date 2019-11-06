# Install https://github.com/cuthbertLab/music21

import music21 as m21
from math import log, log2, pow

# Get standard tuning A4 and bottom C
A4 = 440
C0 = A4 * pow(2, -4.75)

note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
note_variants = [None, "Db", None, "Eb", None, None, "Gb", None, "Ab", None, "Bb", None]


def get_freq(note: str = 'A4'):
    assert isinstance(note, str)
    return m21.note.Note(note).pitch.frequency


def get_note_harmonics(note: str, count: int) -> tuple:
    """
    :param note: (string) The note you want the harmonics for
    :param count: (int) The number of harmonics you want to be returned
    :return: (list) Tuples with harmonic note name and respective frequency
    """
    assert isinstance(note, str)
    assert isinstance(count, int)

    harmonics = []
    harmonic_indexes = range(2, count + 2)

    for i in harmonic_indexes:
        harmonic = m21.note.Note(note).pitch.getHarmonic(i)
        harmonics.append(
            (
                "{}{}".format(harmonic.name, harmonic.octave),
                harmonic.frequency,
                harmonic.frequency % 440,
                harmonic.frequency / 440
            )
        )

    return tuple(harmonics)

# Example
harmonics = []
for note in ('C4', 'E4', 'G4'):
    harmonics.append(
        [note,
        get_note_harmonics(note, 3)]
    )

for i in harmonics:
    print("Note:\t{}\nHarmonics:\t{}\n".format(i[0], [(x[0], x[1]) for x in i[1]]))
