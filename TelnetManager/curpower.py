'''
Created on 8 Eki 2019

@author: samet.yildiz
'''
'''
Created on 4 Ara 2018

@author: samet.yildiz
'''

from TelnetManager import WlUtility
import matplotlib.pyplot as plt
import numpy as np
import datetime
import tkinter as tk # Python 3 import
from tkinter import  *
import threading
import multiprocessing
import datetime
import time
import os
checkState = True

def tryTssi(meanCount,index,power,chain,channel,bw):
    i=0
    outputList=[]
    out=[] 
    clr=0
    while i< index:
        out.append(samet.transmitTryBCM4366(power, meanCount,chain,channel,bw))
        
        i+=1
    i=0
    outputList.append(out)
    out=[]   
    #print(outputList)

def startTest(channel_str, bw_str, chain_str, power_str):
    print("START: " + str(datetime.datetime.now()))

    out=[]
    #tryTssi(10,10,12)
    
    channels=channel_str.split(",")# [36,52,100,132,149]
    bws= bw_str.split(",")# [36,52,100,132,149]
    antennas= chain_str.split(",")# [36,52,100,132,149]
    powers= power_str.split(",")# [36,52,100,132,149]
    
    #bws=[20]
    #antennas=[0,1,2,3]
    for k in antennas:
        for l in channels:
            for m in bws:
                #print("************ CH" + str(l) + "/"+ str(m) +" ANT-"+str(k)+" ***********")
                for i in powers:
                    tryTssi(3,1,int(i),int(k),int(l),int(m))
    
    print("FINISHED: " + str(datetime.datetime.now()))


    samet.telnetExit()



if __name__ == '__main__':
    countryCodes=["US","US4","AE","AR","AR1","CA",
                  "HK","IL","JO","PH","SA","SG","CH",
                  "DE","DK","ES","FR","FR1","GB","IT",
                  "NL","NO","PL","PL1","PT","SE","TR"]
    #countryCodes=["US","US4","CH","DE","DK","ES","FR","GB","IT","NO","PT","TR","US","US4","SG"]
    #countryCodes=["US","FR","EU"]#,"DE","DK","ES","FR","GB","IT","NO","PT","TR","US","US4","SG"]
    count=0
    while count!=len(countryCodes):
        print(str(count) + "-) *******************************************************************************************")
        print("*********************************** " + countryCodes[count]+ " ***************************************************")
        samet = WlUtility("192.168.2.254","root","")
        samet.sendCommand("env_test setenv COUNTRY_CODE " + countryCodes[count])
        samet.sendCommand("env_test saveenv")
        samet.getOutput()
        print("Set to defaults")
        samet.sendCommand("defaults")
        
        time.sleep(300)
        samet = WlUtility("192.168.2.254","root","")
        
        samet.getOutput()
        samet.sendCommand("env_test getenv COUNTRY_CODE")
        samet.getOutput()
        samet.sendCommand("wl -i wl1 chan_info")
        samet.getOutput()
        samet.sendCommand("wl -i wl0 chan_info")
        samet.getOutput()
        print("Test Start: " + str(datetime.datetime.now()))
        samet.getCountryCode()
        channel_array_5g=[36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161,165]
        for i in channel_array_5g:
            samet.captureCurPower(i, "5GHz", "OFDM")
        
        channel_array_2g=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        for i in channel_array_2g:
            samet.captureCurPower(i, "2.4GHz", "DSSS")
        print("Test End: " + str(datetime.datetime.now()))
        count+=1