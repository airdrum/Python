'''
Created on 9 Eyl 2019

@author: samet.yildiz
'''
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import SELECT_MODE_MULTIPLE
filename='C:\\Users\\samet.yildiz\\git\\Python\\programs\\TestResults.xml'

import xml.etree.ElementTree as ET 

root = ET.parse(filename).getroot()
record = root.findall('Record')
layout1 = []
title = []
value = []
modulation=[]
bandwidth=[]
channel=[]
antenna=[]
for i in range(0,len(record)):
    for type_tag in record[i].findall('item'):
        tmp_title = type_tag.get('title')
        if(tmp_title == "Modulation"):
            modulation.append(type_tag.get('value'))
        elif(tmp_title == "Bandwidth"):
            bandwidth.append(type_tag.get('value'))
        elif(tmp_title == "Channel"):
            channel.append(type_tag.get('value'))
        elif(tmp_title == "Antenna"):
            antenna.append(type_tag.get('value'))

modulation_distinct = list(set(modulation))

bandwidth_distinct = list(set(bandwidth))
channel_distinct = list(set(channel))
antenna_distinct = list(set(antenna))
window_title = ["Modulation","Bandwidth","Channel", "Antenna"]

"""layout1.append([sg.Listbox((window_title), size=(20, 20),select_mode=SELECT_MODE_MULTIPLE),
                sg.Text('Column 1', size=(20, 20))])

layout1.append([sg.Text('Column 1', size=(20, 20)),
               [sg.Listbox((window_title), size=(20, 20),select_mode=SELECT_MODE_MULTIPLE),
               sg.Text('Column 2', size=(20, 20)),
               sg.Listbox((window_title), size=(20, 20),select_mode=SELECT_MODE_MULTIPLE)]])
layout1.append([sg.Submit(tooltip='Click to submit this form'), sg.Cancel()])"""
# ------ Menu Definition ------ #


layout1 = [[sg.Text('List of Criteria')],[sg.Listbox(values=(window_title), size=(10, 20),select_mode=SELECT_MODE_MULTIPLE)]]
    


layout1.append([sg.Submit(tooltip='Click to submit this form'), sg.Cancel()])

window = sg.Window('Transmit Power Data Analysis Tool', layout1, default_element_size=(40, 20), grab_anywhere=False)
event, values = window.Read()

layout31 = []
print(values[0])
for i in values[0]:
    if i=="Modulation":
        item = modulation_distinct
    elif i=="Bandwidth":
        item = bandwidth_distinct
    elif i=="Antenna":
        item = antenna_distinct
    elif i=="Channel":
        item = channel_distinct
            
    layout31.extend([sg.Frame(i,[[sg.Listbox((item), size=(10, 5),select_mode=SELECT_MODE_MULTIPLE)]]
     )])

layout3 =[]
layout3.append(layout31)   

layout3.append([sg.Submit(tooltip='Click to submit this form',button_color=('black', 'yellow')), sg.Cancel()])

window_select = sg.Window('Transmit Power Data Analysis Tool', layout3, default_element_size=(40, 20), grab_anywhere=False)
event2, values_filtered = window_select.Read()

print("values:",values)
print("values2:",values_filtered)
value_to_filter = []
for i in values_filtered:
    print(values_filtered[i])
print(values_filtered[i].count("MCS8NSS1"))

for i in range(0,len(record)):
    print(record[i])
    title_element = []
    value_element = []
    for type_tag in record[i].findall('item'):
        title_element.append(type_tag.get('title'))
        value_element.append(type_tag.get('value'))
    print("Title_element:",title_element)
    print("value_element:",value_element)
    print("values_filtered:",values_filtered)
    
    for inval in values_filtered:
        for ink in value_element:
            print(values_filtered[inval].count(ink))
    
    ind = title_element.index("POWER")
    if(values_filtered[i].count(value)):
        value_to_filter.append(type_tag.get('value'))



#mylist = list(set(values))
print(values[0])