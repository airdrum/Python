'''
Created on 9 Eyl 2019

@author: samet.yildiz
'''
filename='C:\\Users\\samet.yildiz\\git\\Python\\programs\\TestResults.xml'

import xml.etree.ElementTree as ET 

root = ET.parse(filename).getroot()
record = root.findall('Record')
print(len(record))
for i in range(0,len(record)):
    count=1
    for type_tag in record[i].findall('item'):
        title = type_tag.get('title')
        value = type_tag.get('value')
        if title=="POWER":
            print("*********" +str(count) + "Berkant, bak bu title ismi: " + title+", Bu da value:" + value)
        
        count+=1