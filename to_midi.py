# handles all things related to MIDI object (notes and mid file)

# requires midiutil module https://pypi.org/project/MIDIUtil/
# based off of example code in the module website (above link)
from midiutil import MIDIFile as midi
import os

class Midi:
    ''' a Midi class that makes the midiutil more usable '''

    def __init__(self, tracks_number, tempo):
        ''' 
        inits midi object, must specify number of 
        tracks and tempo at the start of the piece
        '''

        # inits
        self.track    = 0
        self.channel  = 0
        self.time     = 0    # In beats
        self.tempo    = tempo   # In BPM
        self.volume   = 100  # 0-127, as per the MIDI standard (default)

        # notes is a array of distinct notes (can be chords) that belong to a track
        self.notes    = []  # MIDI note number

        # duration of the notes (corresponds 1-1) to the notes (zips)
        self.duration = []    # In beats

        # midi object init
        self.midi     = midi(tracks_number)  # One track, defaults to format 1 (tempo track is created automatically)

        # inits tempo
        self.set_tempo(self.time, self.tempo)

    def __repr__(self):
        tmp = zip(self.notes, self.duration)
        return f'{tmp}'

    def set_tempo(self, time, tempo):
        ''' sets tempo of track at a given time given the time and the tempo '''
        self.midi.addTempo(self.track, time, tempo)

    def set_track(self, track):
        ''' given new track (int) switch to that track '''
        self.track = track
    
    def note_to_midi(self, string_notes):
        ''' converts notes ie G3, Ab5, f#2 (supports octives 0 to 9 inclusive)
        to notes interperated by this midi class '''

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
        
        if isinstance(string_notes, str):
            string_notes = string_notes.strip().lower()
            return increment + (12 * int(string_notes[-1:]) + key[string_notes[:-1]])

        return_list = []
        for note in string_notes:
            if note != 'r':
                note = note.strip().lower()
                return_list.append(12 * int(note[-1:]) + key[note[:-1]])
            else:
                return_list.append('r')

        return return_list

    def push_notes(self, new_notes, duration):
        ''' 
        given note pitch and duraction, push to self 
        (new note pitch can be a list or a single note, same with duration) 
        '''
        if isinstance(new_notes, list):
            for note, dur in zip(new_notes, duration):
                self.notes.append(note)
                self.duration.append(dur)
        else:
            self.notes.append(new_notes)
            self.duration.append(duration)

    def encode_track(self):
        ''' encodes the entirety of a single track '''
        for note, duration in zip(self.notes, self.duration):
            if isinstance(note, tuple):
                for single_note, single_duraction in zip(note, duration):
                    self.midi.addNote(self.track, self.channel, single_note, self.time, single_duraction, self.volume)
            else:
                if note != 'r':
                    self.midi.addNote(self.track, self.channel, note, self.time, duration, self.volume)

            # calculates new time
            self.time += duration

    def output_mid(self, name):
        '''
        given mid output name (.mid extension not needed), 
        the midi will be written out
        '''

        # format output name
        name = name.strip()
        if name[4:] != '.mid':
            name += '.mid'

        # create directory if note existing
        if not os.path.exists('output'):
            os.makedirs('output')

        new_path = os.path.join('output', name)

        # write to output
        with open(new_path, "wb") as fp:
            self.midi.writeFile(fp)
