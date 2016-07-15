__author__ = 'ekibalko'
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='C:/temp/de-ru.lesx')
root = tree.getroot()

counter=0
for child in root[1].findall('card'):
    counter = counter + 1
    print(child.find('question').text, child.find('answer').text)
    print(counter)

