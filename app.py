import xml.etree.ElementTree as ET
tree = ET.parse('djvu.xml')
# root contains the head tag i.e 
root = tree.getroot()
keyword = "copyright"
#Iterating over each tag called OBJECT
for x in root.iter('OBJECT'):
    # Iterating over each WORD tag to locate the keyword
    for i in x.iter('WORD'):
        if(i.text == keyword):
            '''
                x[0].attrib['value'] is Descartes-TheGeometry_0273.djvu 
                splitting twice at _ and . to extract the page number in this case page number is 0273
            '''
            param = x[0].attrib['value'].split('_')[1] 
            param = param.split('.')[0]
            # page number starts from 0
            print("Keyword",keyword,"found at","page",param)

