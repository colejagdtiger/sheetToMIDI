from to_midi import Midi

def main():
    mid = Midi(1, 115)

    parts = ["B4", "C#5", "D5", "D5", "E5", "c#5", "b4", "a4", "r"] + ["B4", "B4", "C#5", "D5", "a4" , "d5", "a5", "a5", "E5"]
    dur_parts = [.5, .5, .5, .5, .5, .5, .25, 1, .5] + [.5, .5, .5, .5, 1, .5, 1, .5, 2]

    notes = mid.note_to_midi(parts)

    mid.push_notes(notes, dur_parts)
    print(mid)

    mid.encode_track()
    mid.output_mid("test")

if __name__ == "__main__":
    main()
