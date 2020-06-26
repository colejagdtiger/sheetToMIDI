# handles all things related to MIDI object (notes and mid file)

# requires midiutil module https://pypi.org/project/MIDIUtil/
# based off of example code in the module website (above link)
from midiutil import MIDIFile as midi

class Midi:
    ''' a Midi class that makes the midiutil more usable '''

    def __init__(tracks_number, tempo):
        # inits midi object, must specify number of 
        # tracks and tempo at the start of the piece

        # notes is a array of distinct notes (can be chords) that belong to a track
        self.notes    = []  # MIDI note number

        # duration of the notes (corresponds 1-1) to the notes (zips)
        self.duration = []    # In beats

        # inits
        self.track    = 0
        self.channel  = 0
        self.time     = 0    # In beats
        self.tempo    = tempo   # In BPM
        self.volume   = 100  # 0-127, as per the MIDI standard (default)

        # midi object init
        self.midi     = midi(tracks_number)  # One track, defaults to format 1 (tempo track is created automatically)

        # inits tempo
        self.set_tempo(self.time, self.tempo)

    def set_tempo(time, tempo):
        ''' sets tempo of track at a given time given the time and the tempo '''
        self.midi.addTempo(self.track, time, tempo)

    def push_notes(new_notes, duration):
        if new_notes is list:
            for note in new_notes:
                self.notes.append(note)
        else:
                self.notes.append(note)




    def different_track(track):
        self.track = track

    def write_mid(name):
        for notes, duration in zip(self.notes, self.duration):
            self.midi.addNote(track, channel, pitch, time + i, duration, volume)

        with open(name, "wb") as fp:
            self.midi.writeFile(fp)
