import xml.etree.ElementTree as ET

data = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

# get main tag from xml file
# mytree = ET.parse("sample.xml")
# print(mytree.getroot())



# parse from string
mytree = ET.fromstring(data)

# get main tag
root = mytree.tag

# geting first child
root = mytree[0].tag

# print attribute of a tag
root = mytree[0].attrib
print(root)

# print text of a tag
root = mytree[0].text
print(root)

# find and loop through using similar tags
for i in mytree[0].findall("rank"):
	print(i.tag, i.text) 

# loop through tags and find child tags
for i in mytree.findall("country"):
	rankTag = i.find('rank').tag
	rankText = i.find('rank').text
	print(rankTag, rankText) 


# loop through tags and find child tags
for i in mytree.findall("country"):
	des = 'description'
	rankTag = i.find('rank').tag
	rankText = i.find('rank').text
	print(rankTag, rankText) 



