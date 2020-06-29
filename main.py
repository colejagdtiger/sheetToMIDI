'''
Sheet Music to MIDI by 
Coleton Kotch (https://github.com/colejagdtiger) and 
Andrew Li (https://github.com/Zeyu-Li)

Sheet Music to MIDI is a program that transforms 
sheet music (svg or png) to a MID file with separate tracks
'''
from Midi_interface.Midi import Midi

# XML decoder for SVG
import xml.etree.ElementTree as ET


def main():

    tree = ET.parse('input/score_1.svg')

    remove_classes = ['Text', 'SlurSegment', 'BarLine', 'Harmony']

    # additional classes (uncomment next two lines to be removed)
    # additional_classes = ['Stem', 'TimeSig']
    # remove_classes += additional_classes


    # from svg to paths of notes and others
    for path in tree.getroot():
        className = path.get('class')
        if className not in remove_classes:
            print(f'{className}: {path.get("d")}\n')


if __name__ == "__main__":
    main()
