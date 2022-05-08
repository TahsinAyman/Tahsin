import xml.etree.ElementTree as etree


def get_attr_number(node):
    sum = len(node.attrib)
    return sum + get_attr_number()


if __name__ == '__main__':
    tree = etree.parse('data_files\\data1.xml')
    root = tree.getroot()
    print(get_attr_number(root))
