from Midi_interface.Midi import Midi

def main():
    mid = Midi(1, 170)
    
    mid.set_instrument(100)

    parts = [("F5", "G#5", "c5", "D#5"),]*3 + [("A#5", "G5", "c5", "D#5"),] * 2 + [("A#5", "G5", "c6", "D#5"),] * 6
    dur_parts = [1.5, 1.5, 1, 1.5, 1.5] + [1.5] * 6

    new_dur = []
    for part in dur_parts:
        new_dur.append(tuple([part] * 4))

    notes = notes_to_midi(parts)

    mid.push_notes(notes, new_dur)

    mid.output_mid("test2")


def notes_to_midi( string_notes):
    '''
    converts list of notes ie [G3, Ab5, f#2] (supports octives 0 to 9 inclusive)
    to notes interperated by this midi class
    '''

    # key for increment number
    key = {
        'c': 0,
        'c#': 1,
        'db': 1,
        'd': 2,
        'd#': 3,
        'eb': 3,
        'e': 4,
        'fb': 4,
        'e#': 5,
        'f': 5,
        'f#': 6,
        'gb': 6,
        'g': 7,
        'g#': 8,
        'ab': 8,
        'a': 9,
        'a#': 10,
        'bb': 10,
        'b': 11,
        'cb': 11,
        'b#': 0
    }

    return_list = []
    for note in string_notes:
        if isinstance(note, tuple):
            tmp = []
            for single_note in note:
                single_note = single_note.strip().lower()
                tmp.append(12 * int(single_note[-1:]) + key[single_note[:-1]])
            return_list.append(tuple(tmp))
        else:
            if note != 'r':
                note = note.strip().lower()
                return_list.append(12 * int(note[-1:]) + key[note[:-1]])
            else:
                return_list.append('r')

    return return_list

if __name__ == "__main__":
    main()
