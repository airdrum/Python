'''
Created on 9 Eyl 2019

@author: samet.yildiz
'''
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import SELECT_MODE_MULTIPLE
filename='.\\TestResults.xml'

import xml.etree.ElementTree as ET 
from scipy import stats  
import numpy as np  
import matplotlib.pylab as plt2
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.ticker as ticker
from matplotlib.pyplot import legend
import matplotlib
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from scipy import stats
from sklearn.utils.extmath import density



def dataFilter(record):
    samet = []
    for i in range(0,len(record)):
        mainData = []
        expected=""
        power=""
        for type_tag in record[i].findall('item'):
            title_element = []
            
            if(type_tag.get('title')=="ExpectedPower"):
                expected = type_tag.get('value')
            elif(type_tag.get('title')=="POWER"):
                power = type_tag.get('value')
            title_element.append(type_tag.get('title'))
            title_element.append(type_tag.get('value'))
            mainData.append(title_element)
        title_element = ["Delta"]
        x = round(float(power.replace(',','.')) - float(expected.replace(',','.')),2)  
        title_element.append(str(x))
        mainData.append(title_element)
        samet.append(mainData)
    return samet
    
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
selection_criteria = values[0]
print("values         : ",selection_criteria)
print("values_filtered: ",values_filtered)
value_to_filter = []
for i in values_filtered:
    print(values_filtered[i])

original_data = dataFilter(record)

delta = []
for element in original_data:
    criteria = []
    valuesCri = []
    for inner in element:
        criteria.append(inner[0])
        valuesCri.append(inner[1])
    count  = 0
    exist = 1
    for sel in selection_criteria:
        index = criteria.index(sel)
        exist = exist and values_filtered[count].count(valuesCri[index])
        count+=1
    if(exist):
        ind = criteria.index("Delta")
        delta.append(round(float(valuesCri[ind]),2))

print(len(delta))



sns.kdeplot(delta,color='Red', shade=True, label="ANT0")
sns.distplot(delta,color='Red', bins=30)

plt.show()


