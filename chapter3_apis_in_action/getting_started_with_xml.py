#!/usr/bin/env python


"""

Chapter 3: APIs in action
Page: 182

-------------------------

There are two main approaches to working with XML data:

1. Reading in a whole document and creating an object-based representation of it,
   then manipulating it by using an object-oriented API
2. Processing the document from start to end, and performing actions as specific
"""

import xml.etree.ElementTree as ET

# create a xml root element called 'inventory'
root = ET.Element('inventory')
# print it's string representation to screen.
ET.dump(root)  # <inventory /> is an xml shortcut for an empty element '<inventory></inventory>'

# let's put something in the inventory element
# create a new element
cheese = ET.Element('cheese')
# append it to the root element
root.append(cheese)
# print it to screen
ET.dump(root)

# create another element and give it content
# use shortcut class Elementree.SubElement() to create the <name> element and insert it as child of <cheese>
name = ET.SubElement(cheese, 'name')
# git <name> some content by assigning text to the element's text attribute
name.text = 'Caerphilly'
ET.dump(root)

# remove elements by using the remove() method on the parent element
# create a temp element and nest it in the root element
temp = ET.SubElement(root, 'temp')
# print string representation to screen
ET.dump(root)
# remove <temp> from root element tree
root.remove(temp)
# print string representation to screen
ET.dump(root)