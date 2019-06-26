import telnetlib
import sys,os
import time
import re 
from statistics import mean , stdev
from _winapi import ReadFile
import xlsxwriter
from openpyxl import load_workbook
import math
import shutil
class StargateParser:
        # Initializer / Instance Attributes
    def __init__(self,filepath):
        self.filepath = filepath
        self.workbook = xlsxwriter.Workbook("Air4920_new_MVG_oversampled.xlsx")
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

    def readFileColumn(self,fileName,col):
        file = open(fileName, "r")
        fileStr = file.read()
        numarray=[]
        for str in fileStr.splitlines()[4:]:
            numbers = str.split('\t')
            numarray.append((numbers[col-1]))
        return numarray
    
    def readSimulationColumn(self,fileName,col):
        file = open(fileName, "r")
        fileStr = file.read()
        numarray=[]
        for str in fileStr.splitlines()[2:]:
            x=" ".join(str.split())
            numbers = x.split(' ')[col-1]
            first=numbers.split('e')[0]
            power=numbers.split('e')[1]
            x=float(first)*10**(int(power))
            numarray.append(round(x,2))
        return numarray
    def readFileTheta(self,fileName):
        file = open(fileName, "r")
        fileStr = file.read()
        numarray=[]
        for str in fileStr.splitlines()[4:]:
            numbers = str.split('\t')
            numarray.append((numbers[0]))
        return numarray
    def readFileThetaPol(self,fileName):
        file = open(fileName, "r")
        fileStr = file.read()
        numarray=[]
        for str in fileStr.splitlines()[4:]:
            numbers = str.split('\t')
            numarray.append((numbers[3]))
        return numarray
    
    def readFilePhiPol(self,fileName):
        file = open(fileName, "r")
        fileStr = file.read()
        numarray=[]
        for str in fileStr.splitlines()[4:]:
            numbers = str.split('\t')
            numarray.append((numbers[4]))
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
                #worksheet.write(innerlen,arraylen,float(finalarray[arraylen][innerlen]))
                worksheet.write(innerlen,arraylen,round(float(finalarray[arraylen][innerlen]),2))
                arraylen+=1   
            innerlen+=1
            
    def createCombinedExcelTheta(self, parser):
        worksheet = self.workbook.add_worksheet()  
        i=0
        finalarray=[]
        finaltheta=[]
        print(len(parser.listFiles()))
        while i < len(parser.listFiles()):
            pathFile = parser.getAbsolutePath(parser.listFiles()[i])
            
            print("************************************************")
            print(pathFile)
            finalarray.append(parser.readFile(pathFile))
            finaltheta.append(parser.readFileTheta(pathFile))
            print("************************************************")
                                  
            i+=1
        arraylen = 0#len(finalarray)
        while arraylen < len(finalarray):
            x=0
            innerlen = 0
            while innerlen <len(finalarray[0]):
                x += (math.sin(float(finaltheta[arraylen][innerlen])))**2 * (10.0**(float(finalarray[arraylen][innerlen])/10.0))
                innerlen += 1
            arraylen+=1 
            s=float(x)/len(finalarray[0])
            print(10*math.log10(s))

            
    def createCombinedPolTheta(self, parser):
        worksheet = self.workbook.add_worksheet()  
        i=0
        finalarrayTheta=[]
        print(len(parser.listFiles()))
        while i < len(parser.listFiles()):
            pathFile = parser.getAbsolutePath(parser.listFiles()[i])
            
            print("************************************************")
            print(pathFile)
            finalarrayTheta.append(parser.readFileThetaPol(pathFile))
            print("************************************************")
                                  
            i+=1
            
        innerlen = 0#len(finalarray[0])
        while innerlen <len(finalarrayTheta[0]):
            arraylen = 0#len(finalarray)
            while arraylen < len(finalarrayTheta):
                worksheet.write(innerlen,arraylen,round(float(finalarrayTheta[arraylen][innerlen]),2))
                arraylen+=1   
            innerlen+=1
            #print("%.2f" % round(a,2))
    def createCombinedPolPhi(self, parser):
        worksheet = self.workbook.add_worksheet()  
        i=0
        finalarrayPhi=[]
        print(len(parser.listFiles()))
        while i < len(parser.listFiles()):
            pathFile = parser.getAbsolutePath(parser.listFiles()[i])
            
            print("************************************************")
            print(pathFile)
            finalarrayPhi.append(parser.readFilePhiPol(pathFile))
            print("************************************************")
                                  
            i+=1
            
        innerlen = 0#len(finalarray[0])
        while innerlen <len(finalarrayPhi[0]):
            arraylen = 0#len(finalarray)
            while arraylen < len(finalarrayPhi):
                worksheet.write(innerlen,arraylen,round(float(finalarrayPhi[arraylen][innerlen]),2))
                arraylen+=1   
            innerlen+=1
            #print("%.2f" % round(a,2))
    def createCombinedAverage(self, parser):
        worksheet = self.workbook.add_worksheet()  
        i=0
        finalarray4=[]
        finalarray5=[]
        finalarray6=[]
        finalarray7=[]
        finaltheta=[]
        print(len(parser.listFiles()))
        while i < len(parser.listFiles()):
            pathFile = parser.getAbsolutePath(parser.listFiles()[i])
            
            print("************************************************")
            print(pathFile)
            finalarray4.append(parser.readFileColumn(pathFile,4))
            finalarray5.append(parser.readFileColumn(pathFile,5))
            finalarray6.append(parser.readFileColumn(pathFile,6))
            finalarray7.append(parser.readFileColumn(pathFile,7))
            finaltheta.append(parser.readFileColumn(pathFile,2))
                                  
            i+=1
        arraylen = 0#len(finalarray)
        
        while arraylen < len(finalarray4):
            x=0
            innerlen = 0
            average=0
            while innerlen <len(finalarray4[0]):
                forth=10**(float(finalarray4[arraylen][innerlen])/10)
                fifth=10**(float(finalarray5[arraylen][innerlen])/10)
                sixth=10**(float(finalarray6[arraylen][innerlen])/10)
                seventh=10**(float(finalarray7[arraylen][innerlen] )/10)
                theta=float(finaltheta[arraylen][innerlen])
                average+= (forth**2 + fifth**2 ) * math.fabs(math.sin(theta))  
                #x += (math.sin(float(finaltheta[arraylen][innerlen])))**2 * (10.0**(float(finalarray[arraylen][innerlen])/10.0))
                innerlen += 1
            print(average/len(finalarray4[0]))
            arraylen+=1 
            #s=float(x)/len(finalarray[0])
            #print(10*math.log10(s))         

    def closeExcel(self):
        self.workbook.close()
        #return fileStr
    
    def listSimulation(self,ant):
        if ant==0:
            antstr="[1]"
        elif ant==1:
            antstr="[2]"
        elif ant==2:
            antstr="[3]"
            
        fileArray = []
        listfiles=parser.listFiles()
        for i in listfiles:
            if i.find(antstr) == -1:
                continue
            else:
                fileArray.append(self.filepath+'\\'+i)
        
        return fileArray

    def parseSimulation(self, parser, ant):
        worksheet = self.workbook.add_worksheet()  
        i=0
        finalarray=[]
        print(len(parser.listSimulation(ant)))
        while i < len(parser.listSimulation(ant)):
            pathFile = parser.listSimulation(ant)[i]#parser.getAbsolutePath(parser.listSimulation(ant)[i])
            
            print("************************************************")
            print(pathFile)
            finalarray.append(parser.readSimulationColumn(pathFile,3))
            print("************************************************")
                                  
            i+=1
            
        innerlen = 0#len(finalarray[0])
        while innerlen <len(finalarray[0]):
            arraylen = 0#len(finalarray)
            while arraylen < len(finalarray):
                #print(round(float(finalarray[arraylen][innerlen]),2))
                worksheet.write(innerlen,arraylen,round(float(finalarray[arraylen][innerlen]),2))
                arraylen+=1   
            innerlen+=1
            #print("%.2f" % round(a,2))

fileName="E:\\x\\4920_A0X"
parser = StargateParser(fileName)
parser.createCombinedExcel(parser)
parser.filepath ="E:\\x\\4920_A1X"
parser.createCombinedExcel(parser)
parser.filepath ="E:\\x\\4920_A2X"
parser.createCombinedExcel(parser)

"""parser.parseSimulation(parser,0)
parser.parseSimulation(parser,1)
parser.parseSimulation(parser,2)
parser.closeExcel()"""
#parser.createCombinedAverage(parser)
#parser.filepath ="E:\\4921\\4921_A0X"

parser.closeExcel()

