'''
Midi interface by Andrew Li
interface and extension of midiutil
'''

# requires midiutil module https://pypi.org/project/MIDIUtil/
from midiutil import MIDIFile

# os required for output of midi/mid file
import os

class Midi:
    '''
    a Midi class that makes the midiutil more usable,
    *Note: does not support dynamics yet, 
    recommends you export to midi and add dynamics in your midi editor
    '''

    def __init__(self, tracks_number, tempo, volume = 100):
        ''' 
        inits midi object, must specify number of
        tracks and tempo at the start of the piece
        (optional) volume of piece, default to 100
        '''

        # checks if volume is within range
        assert 0 <= int(volume) <= 127, "Volume out of range"

        # inits
        self.track    = 0            # which track
        self.channel  = 0            # very much like a track but limited to 16 slots (tracks contain a maximum of 16 channels)
        self.time     = 0            # in beats
        self.tempo    = int(tempo)   # BPM
        self.volume   = int(volume)  # 0-127, as per the MIDI standard (100 default)

        # notes is a array of distinct notes (can be chords, specified with a tuple) that belong to a track
        self.notes    = []  # MIDI note number

        # duration of the notes (corresponds 1-1) to the notes 
        self.duration = []    # In beats

        # midi object init (private)
        self.__midi     = MIDIFile(int(tracks_number))  # One track, defaults to format 1 (tempo track is created automatically)

        # sets tempo
        self.set_tempo(self.tempo, self.time)

    def __repr__(self):
        ''' prints representation of midi (all the notes and duraction) as a list '''
        return [zip(self.notes, self.duration)]

    def set_tempo(self, tempo, time = 0):
        ''' sets tempo of track at a given time given the time and the tempo, defaults to start of track '''
        self.__midi.addTempo(self.track, time, tempo)

    def set_track(self, track):
        ''' given new track (int) switch to that track '''
        self.track = track

    def set_instrument(self, instrument_number):
        ''' set the instrument of current track; use this website to find your instrument: https://www.midi.org/specifications/item/gm-level-1-sound-set '''
        self.__midi.addProgramChange(self.track, self.channel, self.time, instrument_number)
    
    def notes_to_midi(self, string_notes):
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

    def push_notes(self, new_notes, duration):
        ''' 
        given list of note pitch and duraction, push to notes and duraction attribute
        (new note pitch can be a list or a single note, same with duration)
        '''
        for note, dur in zip(new_notes, duration):
            self.notes.append(note)
            self.duration.append(dur)

    def encode_track(self):
        ''' encodes the entirety of a single track '''

        # for each note and duration, add note
        for note, duration in zip(self.notes, self.duration):
            if isinstance(note, tuple):
                for single_note, single_duraction in zip(note, duration):
                    self.__midi.addNote(self.track, self.channel, single_note, self.time, single_duraction, self.volume)
            else:
                if note != 'r':
                    self.__midi.addNote(self.track, self.channel, note, self.time, duration, self.volume)

            # calculates new time
            if isinstance(duration, tuple):
                self.time += duration[0]
            else:
                self.time += duration

    def output_mid(self, name):
        '''
        given mid output name (.mid extension not needed),
        the .mid extension will be added
        *Note if the mid file of the same name already exists, it will be OVERWRITTEN
        '''

        # encodes current track
        self.encode_track()

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
            self.__midi.writeFile(fp)
