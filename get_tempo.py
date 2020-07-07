def create_tempo(ET, scale, path):
    
    # crafting a new xml file
    tempo = ET.Element('svg')
    # setting height and width
    tempo.set('width', '400')   # scale up by the scale for more clarity
    tempo.set('height', '400')
    tempo.set('xmlns', 'http://www.w3.org/2000/svg')

    new_path = ET.SubElement(tempo, 'path')
    new_path.set('transform', f"scale({scale})")

    new_path.set('d', f'{path}')

    return tempo