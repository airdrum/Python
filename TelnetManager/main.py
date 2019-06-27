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

checkState = True
samet = WlUtility("192.168.2.254","root","Admin123*")
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
def my_function():
        channel_id = channel_entry.get()
        bw_id = bw_entry.get()
        chain_id = chain_entry.get()
        power_id = power_entry.get()
        print("Channels: " + channel_id +", BW: " + bw_id +", Chains: "+chain_id,", Powers: "+power_id)
        
        #thread1 = threading.Thread(target = startTest,args=(channel_id,bw_id,chain_id,power_id))
        process = multiprocessing.Process(target = startTest,args=(channel_id,bw_id,chain_id,power_id))
        #thread1.start()
        process.start()
        #do stuff with url_member
"""
def getFigure(ant,meanCount,index,power):
    array0=np.ones(index)*power
    array1=np.ones(index)*power +0.5
    array2=np.ones(index)*power -0.5
    array3=np.ones(index)*power +1
    array4=np.ones(index)*power -1
    i=0
    channelList=[36]
    #channelList=[36,52,100,132,149]
    outputList=[]
    bw=80
    out=[] 
    color=['r', 'b', 'g', 'k', 'm']
    clr=0
    for ch in channelList:
        while i< index:
            out.append(samet.transmitPowerBCM4360(ch, bw, ant, power, meanCount))
            
            i+=1
        i=0
        #plt.plot(out, '-c', label='Channel'+str(ch)+'/'+str(bw).format(color[clr]))
        clr+=1
        outputList.append(out)
        out=[]    
    for i, color in enumerate(['red', 'black', 'blue', 'brown', 'green'], start=0):
        plt.plot(outputList[i], color=color, label='Channel'+str(channelList[i])+'-'+str(bw))
    
    
    print(outputList)
    plt.legend(loc='upper right', fontsize = 'x-small')
    plt.ylabel('Transmit Power (dBm)')
    plt.xlabel('Calculated Power Index')
    plt.ylim(power-1.5, power+1.5)
    plt.plot(array0, ':c')
    plt.plot(array1, ':k')
    plt.plot(array2, ':k')
    plt.plot(array3, ':k')
    plt.plot(array4, ':k')
    outTitle=str(power) +" dBm ANT"+str(ant)+" with Mean Count: " + str(meanCount)
    plt.title(outTitle)
    plt.savefig(str(power) +" dBm ANT"+str(ant)+" " +str(bw)+" MHz Transmit Power.png", bbox_inches='tight')
    plt.close()
    
    for i, color in enumerate(['red', 'black', 'blue', 'brown', 'green'], start=0):
        plt.hist(outputList[i], bins=50, density=1, facecolor=color, alpha=0.75,label='Channel'+str(channelList[i])+'-'+str(bw))
    plt.legend(loc='upper right', fontsize = 'x-small')
    plt.ylabel('Transmit Power Histogram (dBm)')
    plt.xlabel('Calculated Power Index')
    outTitle=str(power) +" dBm ANT"+str(ant)+" Histogram with Index Count: " + str(index)
    plt.title(outTitle)
    plt.savefig(str(power) +" dBm ANT"+str(ant)+" " +str(bw)+" MHz Transmit Power Histogram.png", bbox_inches='tight')
    plt.close()
"""
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
    
    root = tk.Tk()

    channel_label = tk.Label(root, text = "Channels",font=("Calibri",12))
    
    channel_label.grid(row = 0, column = 0)
    channelText = tk.StringVar()
    channel_entry = tk.Entry(root, textvariable=channelText,font=("Calibri",12))
    channelText.set( "36,52,100,132,149" )
    channel_entry.grid(row = 0, column = 1)
    
    bw_label = tk.Label(root, text = "Bandwidth",font=("Calibri",12))
    bw_label.grid(row = 1, column = 0)
    bwText = tk.StringVar()
    bw_entry = tk.Entry(root, textvariable=bwText,font=("Calibri",12))
    bwText.set( "20,40,80" )
    bw_entry.grid(row = 1, column = 1)
    
    chain_label = tk.Label(root, text = "Chains",font=("Calibri",12))
    chain_label.grid(row = 2, column = 0)
    chainText = tk.StringVar()
    chain_entry = tk.Entry(root, textvariable=chainText,font=("Calibri",12))
    chainText.set( "0,1,2,3" )
    chain_entry.grid(row = 2, column = 1)
    
    power_label = tk.Label(root, text = "Powers",font=("Calibri",12))
    power_label.grid(row = 3, column = 0)
    powerText = tk.StringVar()
    power_entry = tk.Entry(root, textvariable=powerText,font=("Calibri",12))
    powerText.set( "10,13,16,19,22" )
    power_entry.grid(row = 3, column = 1)
    
    my_button = tk.Button(root, text = "Send", command = my_function,font=("Calibri",12))
    my_button.grid(row = 4, column = 1)
    root.mainloop()
    

    
    
    """a1_set = -214
    b0_set = 5816
    b1_set = -719
    search_ind=30
    idle_tssi = -423
    tssi = 81
    adj_tssi = 64.875
    indices =np.arange(-32767,32767)
    a1 = np.arange(a1_set - search_ind,a1_set + search_ind)/(2**15);
    b0 = np.arange(b0_set - search_ind,b0_set + search_ind)/(2**8);
    b1 = np.arange(b1_set - search_ind,b1_set + search_ind)/(2**12);
    
    total_power = []#((b0 + (b1*adj_tssi))/(1+(a1*adj_tssi)))
    power=[]
    a1_s=[]
    b0_s=[]
    b1_s=[]
    for a1_in in a1:
        for b1_in in b1:
            for b0_in in b0:
                x = (b0_in + (b1_in*adj_tssi))/(1+(a1_in*adj_tssi))
                if x <20.01 and x>19.99:
                    tot = str(x)+", a1:"+str(round(a1_in*2**15))+", b0:"+str(round(b0_in*2**8))+", b1:"+str(round(b1_in*2**12))
                    total_power.append(tot)
                    power.append(x)
                    a1_s.append(a1_in*2**15)
                    b0_s.append(b0_in*2**8)
                    b1_s.append(b1_in*2**12)
                    print(tot)
        
    
    values = power
    values[:] = [abs(x - 20) for x in values]
    (m,i) = min((v,i) for i,v in enumerate(values))
    #print ("Index is:"+str(i)+" Power is:"+str(total_power[i])+" a1 is:"+str(a1_s[i])+" b0 is:"+str(b0_s[i])+" b1 is:"+str(b1_s[i]))
    a1_h=hex(int(a1_s[i]) & (2**16-1))
    b0_h=hex(int(b0_s[i]) & (2**16-1))
    b1_h=hex(int(b1_s[i]) & (2**16-1))
    print ("a1 is:"+str(a1_h)+" b0 is:"+str(b0_h)+" b1 is:"+str(b1_h))
    print(hex(-1234& (2**16-1)))"""
                                                                                                                                                                                                                                                                   