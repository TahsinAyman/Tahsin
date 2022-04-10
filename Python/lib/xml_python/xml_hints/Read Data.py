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
print("With Index (List Index):\n")

"""
It Return The Text Like
"<name gender="Male">Tahsin</name>"
Here the "Tahsin" is A text
"""
print(data[0][0].text)
"""
It Returns a Tag Like
"<name gender="Male">Tahsin</name>"
Here The "name" is A Tag
"""
print(data[0][0].tag)
"""
It Returns the Attributes Like
<name gender="Male">Tahsin</name>"
here The "gender" is A Attribute's Key
And "Male" is the Attribute's Value
Example:
{'gender': 'Male'}
Returns A Dictionary
"""
print(data[0][0].attrib)

# Same Examples But Different Code

# Here we search with Names
print("\nWith Find (Function):\n")
name = data.find('person/name')
print(name.text)
print(name.tag)
print(name.attrib)
