from Midi_interface.Midi import Midi

def main():
    mid = Midi(1, 170)
    
    mid.set_instrument(100)

    parts = [("F5", "G#5", "c5", "D#5"),]*3 + [("A#5", "G5", "c5", "D#5"),] * 2 + [("A#5", "G5", "c6", "D#5"),] * 6
    dur_parts = [1.5, 1.5, 1, 1.5, 1.5] + [1.5] * 6

    new_dur = []
    for part in dur_parts:
        new_dur.append(tuple([part] * 4))

    notes = mid.notes_to_midi(parts)

    mid.push_notes(notes, new_dur)

    mid.output_mid("test3")


if __name__ == "__main__":
    main()
