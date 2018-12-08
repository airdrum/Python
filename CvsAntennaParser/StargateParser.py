import telnetlib
import sys,os
import time
import re 

from statistics import mean , stdev
from _winapi import ReadFile
import xlsxwriter
from openpyxl import load_workbook


class StargateParser:
        # Initializer / Instance Attributes
    def __init__(self,filepath):
        self.filepath = filepath
        self.workbook = xlsxwriter.Workbook("output.xlsx")
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
    
    def createCombinedExcel(self, parser):
        worksheet = self.workbook.add_worksheet()  
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
            while arraylen < len(finalarray):
                worksheet.write(innerlen,arraylen,float(finalarray[arraylen][innerlen]))
                arraylen+=1   
            innerlen+=1
         
    def closeExcel(self):
        self.workbook.close()
        #return fileStr
# Create an new Excel file and add a worksheet.

fileName="E:\\4921\\4921_A2X"
parser = StargateParser(fileName)
parser.createCombinedExcel(parser)
parser.filepath ="E:\\4921\\4921_A1X"
parser.createCombinedExcel(parser)
parser.filepath ="E:\\4921\\4921_A0X"
parser.createCombinedExcel(parser)
parser.closeExcel()

"""wb = load_workbook(filename = 'output.xlsx')
ws1 = wb["Sheet1"] # insert at the end (default)
ws2 = wb["Sheet2"] 
ws3 = wb["Sheet3"] 
x1 = ws1.cell(row=3, column=2).value
x2 = ws2.cell(row=3, column=2).value
x3 = ws3.cell(row=3, column=2).value
print(x1+x2+x3)
fileName="E:\\4920"
parser = StargateParser(fileName)
print(fileName + '\\' +parser.listFiles()[0])"""