import xml.etree.cElementTree as ET 

tree = ET.parse('xml-sample.xml')
root = tree.getroot()

print root.tag
print root.attrib

for child in root:
    print child.tag, child.attrib
    
for neighboor in root.iter('neighbor'):
    print neighboor.attrib
    
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank
    
    
    
    