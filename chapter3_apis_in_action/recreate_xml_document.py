#!/usr/bin/env python

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


# creet the root element object
root = ET.Element('inventory')
# add cheese as a sub element of the root tree object
cheese = ET.SubElement(root, 'cheese')
# add an attribute to the cheese sub element object
cheese.attrib['id'] = 'c01'
name = ET.SubElement(cheese, 'name')
name.text = 'Caerphilly'
stock = ET.SubElement(cheese, 'stock')
stock.text = "0"
cheese = ET.SubElement(root, 'cheese')
cheese.attrib['id'] = 'c02'
name = ET.SubElement(cheese, 'name')
name.text = 'Illchester'
stock = ET.SubElement(cheese, 'stock')
stock.text = "0"


def xml_pprint(element):
    # create a string of bytes from the root tree object
    s = ET.tostring(element)
    # use minidom to parse the string and format to pretty xml
    print(minidom.parseString(s).toprettyxml())

xml_pprint(root)


def xml_convert_to_bytes(element):
    # convert xml object to string of bytes
    text = ET.tostring(element)
    print(text)

xml_convert_to_bytes(root)
