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

# rasterize svgs
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

import svgutils
import get_tempo


def svg_to_img(file_name, scale):
    ''' converts a specified svg file to a simplified png file '''

    # format input string
    tempo = ''
    file_name = file_name.strip()
    if file_name[-4:] == '.svg':
        file_name = file_name[:-4]

    tree = ET.parse(f'input/{file_name}.svg')

    remove_classes = ['Text', 'SlurSegment', 'BarLine', 'Harmony', 'StaffLines']

    # additional classes (uncomment next two lines to be removed)
    # additional_classes = ['Stem', 'TimeSig']
    # remove_classes += additional_classes

    # get height + width
    width = tree.getroot().get('width')
    height = tree.getroot().get('height')

    # crafting a new xml file
    main = ET.Element('svg')
    # setting height and width
    main.set('width', str(float(width)*scale))   # scale up by the scale for more clarity
    main.set('height', str(float(height)*scale))
    main.set('xmlns', 'http://www.w3.org/2000/svg')


    # from svg to paths of notes and others while removing some unused paths
    for path in tree.getroot():
        className = path.get('class')
        if className not in remove_classes:

            # new path
            new_path = ET.SubElement(main, 'path')
            if className not in ['Note', 'Hook', 'Beam', 'Rest', 'NoteDot']:
                new_path.set('stroke-width', ".36")
                new_path.set('fill', "none")
                new_path.set('stroke', "#000")

            if className == 'Tempo':
                tempo = get_tempo.create_tempo(ET, scale, path.get("d"))
                ET.ElementTree(tempo).write(f'tmp/tempo1.svg')

            new_path.set('transform', f"scale({scale})")

            # show names for debuging purposes
            new_path.set('class', className)
            
            # sets path
            new_path.set('d', f'{path.get("d")}')

    # print final product
    # print(ET.tostring(main))
    
    # write to file
    # ET.ElementTree(main).write(f'tmp/{file_name}.svg')

    # drawing = svg2rlg(f'tmp/{file_name}.svg')
    # renderPM.drawToFile(drawing, f'tmp/{file_name}.png', fmt="PNG")


def main():
    # file name here
    svg_file = 'score_1'
    scale = 4

    # converts svg to png
    svg_to_img(svg_file, scale)

    # Output midi
    # sets track and tempo

    # get tempo by text recognition (using openCV) on the BPM

    # get number of tracks by getting a small sliver of the bar lines right beside the time signature
    # and seeing the distance between the 5 bar lines
    # mid = Midi(1, 170)

    # set random instrument
    # mid.set_instrument(100)

    # image recognition, one pass for the pitch and one pass for the duration
    # parts = [("F5", "G#5", "c5", "D#5"),]*3 + [("A#5", "G5", "c5", "D#5"),] * 2 + [("A#5", "G5", "c6", "D#5"),] * 6
    # dur_parts = [1.5, 1.5, 1, 1.5, 1.5] + [1.5] * 6

    # new_dur = []
    # for part in dur_parts:
    #     new_dur.append(tuple([part] * 4))

    # notes = mid.notes_to_midi(parts)

    # mid.push_notes(notes, new_dur)

    # mid.output_mid("test3")


if __name__ == "__main__":
    main()
