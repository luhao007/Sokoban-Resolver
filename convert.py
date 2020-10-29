import os
import re

from defusedxml import ElementTree, minidom
from xml.etree.ElementTree import Element, SubElement


def convert(folder):
    root = Element('SokobanLevels')
    title = SubElement(root, 'Title')
    title.text = folder.split('/')[-1]
    desc = SubElement(root, 'Description')
    desc.text = folder.split('/')[-1]
    collection = SubElement(root, 'LevelCollection')
    i = 1

    def natural_keys(text):
        return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]

    for file in sorted(os.listdir(folder), key=natural_keys):
        if not file.endswith('.txt'):
            continue

        level = SubElement(collection, 'Level', {'id': str(i)})

        with open('/'.join([folder, file]), 'r') as f:
            for r in f.readlines():
                line = SubElement(level, 'L')
                line.text = r[:-1].rstrip()

        i += 1

    s = ElementTree.tostring(root, encoding='utf-8', xml_declaration=False)
    parsed = minidom.parseString(s)
    xml = parsed.toprettyxml(indent='  ', encoding='utf-8', newl='\n')

    with open(f'{folder}.slc', 'wb') as f:
        f.write(xml)
