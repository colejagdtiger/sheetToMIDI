def create_tempo(ET, scale, path):
    ''' created tempo '''

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

def vision(file_name):
    ''' reads number from file '''
    import cv2
    import pytesseract
    import re

    config = ('-l eng --oem 1 --psm 3')

    im = cv2.imread(file_name, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(im, config=config)

    text = re.search('=(.+)', text)
    
    if text:
        text = text.group(1).strip()
        try:
            text = int(text)
        except Exception:
            return None
    else:
        return None

    return text
