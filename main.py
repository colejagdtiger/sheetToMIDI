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


def main():

    file_name = 'score_1'

    # format input string
    file_name = file_name.strip()
    if file_name[-4:] == '.svg':
        file_name = file_name[:-4]

    tree = ET.parse(f'input/{file_name}.svg')

    remove_classes = ['Text', 'SlurSegment', 'BarLine', 'Harmony']

    # additional classes (uncomment next two lines to be removed)
    # additional_classes = ['Stem', 'TimeSig']
    # remove_classes += additional_classes

    # get height + width
    width = tree.getroot().get('width')
    height = tree.getroot().get('height')

    # crafting a new xml file
    main = ET.Element('svg')
    # setting height and width
    main.set('width', width)
    main.set('height', height)
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

            # show names for debuging purposes
            new_path.set('class', className)
            
            # sets path
            new_path.set('d', f'{path.get("d")}')

    # print final product
    # print(ET.tostring(main))
    
    # write to file
    ET.ElementTree(main).write(f'tmp/{file_name}.svg')

    drawing = svg2rlg(f'tmp/{file_name}.svg')
    renderPM.drawToFile(drawing, f'tmp/{file_name}.png', fmt="PNG")

if __name__ == "__main__":
    main()
