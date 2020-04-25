from lxml import etree
parser = etree.XMLParser(recover=True)
tree = etree.parse('djvu.xml',parser)
# search is case sensitive "africa" wont be detected
keyword = "AFRICA"
#Iterating over each tag called OBJECT
for x in tree.iter('OBJECT'):
    # Iterating over each WORD tag to locate the keyword
    for i in x.iter('WORD'):
        if(i.text == keyword):
            '''
                x[0].attrib['value'] is Descartes-TheGeometry_0273.djvu 
                splitting twice at '.' and finding the last 4 lettes of the book name in this case it is 0273
            '''
            param = x[0].attrib['value'].split('.')[0] 
            param = param[-4:]
            
            print("Keyword",i.text,"found at","page",param)
