import xml.etree.ElementTree as et

mytree = et.parse('sample.xml')
root = mytree.getroot()
print(root)




