# Install https://github.com/cuthbertLab/music21

import music21 as m21
from math import log, log2, pow

# Get standard tuning A4 and bottom C
A4 = 440
C0 = A4*pow(2, -4.75)

note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
note_variants = [None, "Db", None, "Eb", None, None, "Gb", None, "Ab", None, "Bb", None]


def get_note(freq):
    # half_steps = round(12*log2(freq/C0))
    half_steps = round(12 * log(freq / C0, 2))
    octave = half_steps // 12
    n = half_steps % 12
    return "{}{}".format(note_names[n], octave)

def get_freq(note, octave):
    index = note_names.index(note)
    half_steps = octave * 12
