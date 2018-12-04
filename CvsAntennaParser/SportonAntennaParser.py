'''
Created on 30 Kas 2018

@author: samet.yildiz
'''
import telnetlib
import sys,os
import time
import re 

from statistics import mean , stdev
import os,sys
from pip._vendor.html5lib._ihatexml import ideographic
 
path = '.' 

    
class SportonAntennaParser:
        # Initializer / Instance Attributes
    def __init__(self,filepath):
        self.filepath = filepath
        
    def listFiles(self):
        fileArray = []
        if len(sys.argv) == 2:
            self.filepath  = sys.argv[1]
 
        files = os.listdir(self.filepath)
        for name in files:
            fileArray.append(name)

        return fileArray
    
    def getAbsolutePath(self,file):
        absFile=self.filepath + '\\' +(file)
        return absFile
parser = SportonAntennaParser("C:\\Users\\samet.yildiz\\Dropbox\AirTies\\antenna")

file = open(parser.getAbsolutePath(parser.listFiles()[0]), "r")
fileStr = file.read()
totalFile = fileStr.splitlines()[15:]

phi=[]
output = []
angle=[]
frequency = ""
mainOut=[]
theta=[]
response=[]
for line in totalFile:
    

    step = line.split(',')

    
    samet=0
    if step[2] == "Theta Angle  (?":
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            theta.append(step[ind])
            ind+=1
        #print(theta)
    elif step[2] == '0':
        phi.append('0')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('0,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '15':
        phi.append('15')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('15,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '30':
        phi.append('30')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('30,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '45':
        phi.append('45')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('45,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '60':
        phi.append('60')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('60,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '75':
        phi.append('75')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('75,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '90':
        phi.append('90')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('90,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '105':
        phi.append('105')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('105,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '120':
        phi.append('120')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('120,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '135':
        phi.append('135')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('135,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '150':
        phi.append('150')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('150,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '165':
        phi.append('165')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('165,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '180':
        phi.append('180')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('180,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '195':
        phi.append('195')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('195,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '210':
        phi.append('210')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('210,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '225':
        phi.append('225')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('225,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '240':
        phi.append('240')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('240,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '255':
        phi.append('255')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('255,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '270':
        phi.append('270')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('270,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '285':
        phi.append('285')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('285,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '300':
        phi.append('300')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('300,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '315':
        phi.append('315')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('315,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 
    elif step[2] == '330':
        phi.append('330')
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('330,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response)
    elif step[2] == '345':
        ind=3
        while ind < len(step):
            if step[ind] =='':
                break
            print('345,'+theta[ind-3]+',' +step[ind])
            ind+=1
        #print(response) 

    k = 0
    """while k < len(step):
        if step[k]=="Theta Angle  (?":
            print(step[k])
        
        k+=1"""
    #print(step)
