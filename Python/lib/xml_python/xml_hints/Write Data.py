"""
xml Data (Read)
==========================================================================
<root>
    <person>
        <name gender="Male">Tahsin</name>
        <age>12</age>
    </person>
</root>
==========================================================================
"""

from xml.etree import ElementTree
import os
import sys

xml = ElementTree.parse('data\\Read Data.xml')
# The File Must be There
data = xml.getroot()
# With Index (List Index):

"""
We change the Value of A Variable Like
<name gender="Male">Tahsin</name>
Here "Tahsin" changes with "Tasmiah"
so The Value is
<name gender="Male">Tasmiah</name>
"""

data[0][0].text = "Tasmiah"

"""
We change the Variable Name Like
<name gender="Male">Tasmiah</name>
Here "name" changes with "person_name"
so The Value is
<person_name gender="Male">Tasmiah</person_name>
"""

data[0][0].tag = "person_name"

"""
We change the Variable's Attribute Name Like
<name gender="Male">Tasmiah</name>
Here "gender" changes with "person_gender" (The Dictionary's[0] Key)
Here "Male" changes with "Female" (The Dictionary's[1] Key)
so The Value is
<person_name person_gender="Male">Tasmiah</person_name>
"""

data[0][0].attrib = {'person_gender': 'Female'}

# Same With Other Example
# With Find (Function):
name = data.find('person/person_name')
name.text = "Tasmiah"
name.tag = "person_name"
name.attrib = {'person_gender': 'Female'}

xml.write('data\\Write Data.xml')
# If The File Isn't there It will Create One
"""
xml Data (Write)
==========================================================================
<root>
    <person>
        <person_name person_gender="Female">Tasmiah</person_name>
        <age>12</age>
    </person>
</root>
==========================================================================
"""
