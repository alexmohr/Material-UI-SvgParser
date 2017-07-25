import os.path
import sys
import xml.etree.ElementTree as ET
def __init__():
    pass

def get_icon_svg_path(name):
    name_parts = name.split(".")
    file_path = os.path.join(os.path.dirname(sys.argv[0]), '..', 'lib', 'material-design-icons',
                            name_parts[0], "svg", "production",
                             "ic_" + name_parts[1] + "_24px.svg")

    file = open(file_path, 'r')
    data = file.read()
    xml = ET.fromstring(data)
    print(xml[0].attrib["d"])


