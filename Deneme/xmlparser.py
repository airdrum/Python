'''
Created on 19 Tem 2019

@author: samet.yildiz
'''


filename='C:\\Users\samet.yildiz\\OneDrive - airties.com\\PA Trimming\\4960_PA_Trimming\\airties.xml'

import xml.etree.ElementTree as ET 

root = ET.parse(filename).getroot()
record = root.findall('Record')
print(len(record))
for i in range(0,len(record)):
    count=1
    for type_tag in record[i].findall('item'):
        title = type_tag.get('title')
        value = type_tag.get('value')
        print("*********" +str(count) + "Berkant, bak bu title ismi: " + title+", Bu da value:" + value)
        count+=1
    print("-------------------------------------")
"""xtree = et.parse(filename)
xroot = xtree.getroot() 

print(xroot.tag)
for node in xroot: 
    if node.tag == "Record":
        for neighbor in node.iter('title'):
            print(neighbor.attrib)
        
    

    print("********")
"""