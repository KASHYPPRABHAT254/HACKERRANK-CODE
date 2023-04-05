import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = 0
    count = count + len(node.attrib)
    for child in node:
        if(len(child.tag)!=0):
            for i in child:
                count = count + len(i.attrib)
        count = count + len(child.attrib)
    return count
        
    # your code goes here
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
