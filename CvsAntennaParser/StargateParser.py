import telnetlib
import sys,os
import time
import re 

from statistics import mean , stdev
from _winapi import ReadFile
import xlsxwriter



class StargateParser:
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
    
    def readFile(self,fileName):
        file = open(fileName, "r")
        fileStr = file.read()
        numarray=[]
        for str in fileStr.splitlines()[4:]:
            numbers = str.split('\t')
            numarray.append((numbers[2]))
        return numarray
        #return fileStr
# Create an new Excel file and add a worksheet.

fileName="E:\\4920_A0X"
parser = StargateParser(fileName)
excelName = fileName + '\\' + fileName.split('E:\\')[1] + '.xlsx'
print(excelName)
workbook = xlsxwriter.Workbook(excelName)
worksheet = workbook.add_worksheet()  

i=0
finalarray=[]
print(len(parser.listFiles()))
while i < len(parser.listFiles()):
    pathFile = parser.getAbsolutePath(parser.listFiles()[i])
    
    print("************************************************")
    print(pathFile)
    finalarray.append(parser.readFile(pathFile))
    print("************************************************")
                          
    i+=1
    
innerlen = 0#len(finalarray[0])
while innerlen <len(finalarray[0]):
    arraylen = 0#len(finalarray)
    w=""
    while arraylen < len(finalarray):
        worksheet.write(innerlen,arraylen,finalarray[arraylen][innerlen])
        arraylen+=1   
    innerlen+=1
  
    
workbook.close()