from xml.etree import ElementTree

xml = ElementTree.parse('F:\\Workspace\\Tahsin\\Python\\lib\\xml_python\\data\\human.xml')
data = xml.getroot()

for i in data:
	string = i.text.strip()
#=
	print(string)


