from xml.etree import ElementTree
from time import sleep as delay

xml = ElementTree.parse("data\\New Data.xml")

data = xml.getroot()

# for i in data:
#     ElementTree.SubElement(i, 'Classes')
#     classes = i.find('Classes')
#     classes.text = "1-10"
#     classes.set('start', '1')
#
# xml.write('data\\New Data.xml')
# delay(5)
for i in data:
    classes = i.find('Classes')
    classes.attrib.pop('start')
    delay(3)
    i.remove(classes)
xml.write('data\\New Data.xml')
