from Midi_interface.Midi import Midi

def main():
    # sets 1 track and tempo as 115 bpm
    mid = Midi(1, 115)
    
    # sets instrument as guitar
    mid.set_instrument(25)

    parts = ["B4", "C#5", "D5", "D5", "E5", "c#5", "b4", "a4", "r"] + ["B4", "B4", "C#5", "D5", "a4" , "d5", "a5", "a5", "E5"]
    dur_parts = [.5, .5, .5, .5, .5, .5, .25, 1, .5] + [.5, .5, .5, .5, 1, .5, 1, .5, 2]

    # translate notes
    notes = mid.notes_to_midi(parts)

    # push notes and duration to stack
    mid.push_notes(notes, dur_parts)

    # output to file named test
    mid.output_mid("test")

if __name__ == "__main__":
    main()
