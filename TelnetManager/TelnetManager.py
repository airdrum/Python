
import telnetlib
import sys,os
import time
import re 





antenna_power_0=""
antenna_power_1=""
antenna_power_2=""

class WlUtility:
        # Initializer / Instance Attributes
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        
    def telnetGetWlData(self,key,count,sleep_time):
        
        tn = telnetlib.Telnet(self.host)
        tn.read_until(b"login: ")
        tn.write(self.user.encode('ascii') + b"\n")
        if self.password:
            tn.read_until(b"Password: ")
            tn.write(self.password.encode('ascii') + b"\n")
        i=0
    
        while i<count:
            tn.write(key)
            time.sleep(sleep_time)
            i+=1
        tn.write(b"exit\n")
        output = tn.read_all().decode('ascii')
        #print(output)
        data = output.split('\r')
        i=0
        my_list = []
        for temp in data:
            i=i+1
            if key.decode("utf-8")[:-1] in temp:
                my_list.append(data[i])
        return my_list
    
    def s16(self,value):
        return -(value & 0x8000) | (value & 0x7fff)
    
    def telnetAllTssiWlDataBCM4360(self,count):

        phy_test_tssi_0 = b"wl -i wl1 phy_test_tssi 0\n"
        phy_test_tssi_1 = b"wl -i wl1 phy_test_tssi 1\n"
        phy_test_tssi_2 = b"wl -i wl1 phy_test_tssi 2\n"
        phy_test_idletssi_0 = b"wl -i wl1 phy_test_idletssi 0\n"
        phy_test_idletssi_1 = b"wl -i wl1 phy_test_idletssi 1\n"
        phy_test_idletssi_2 = b"wl -i wl1 phy_test_idletssi 2\n"
        getenv0=b"env_test getenv 1:pa5ga0\n"
        getenv1=b"env_test getenv 1:pa5ga1\n"
        getenv2=b"env_test getenv 1:pa5ga2\n"
        tn = telnetlib.Telnet(self.host)
        tn.read_until(b"login: ")
        tn.write(self.user.encode('ascii') + b"\n")
        if self.password:
            tn.read_until(b"Password: ")
            tn.write(self.password.encode('ascii') + b"\n")
        i=0
        tn.write(b"iwconfig\r\n")
        tn.write(getenv0)
        tn.write(getenv1)
        tn.write(getenv2)
        while i<count:
            tn.write(phy_test_tssi_0)
            tn.write(phy_test_tssi_1)
            tn.write(phy_test_tssi_2)
            tn.write(phy_test_idletssi_0)
            tn.write(phy_test_idletssi_1)
            tn.write(phy_test_idletssi_2)
            time.sleep(0.1)
            i+=1
        tn.write(b"exit\n")
        output = tn.read_all().decode('ascii').replace('\n','')
        #print(output)
        data = output.split('\r')
        i=0
        tssi_0 = []
        tssi_1 = []
        tssi_2 = []
        idletssi_0 = []
        idletssi_1 = []
        idletssi_2 = []
        pa5ga0 = ""
        pa5ga1 = ""
        pa5ga2 = ""
        samet =[]
        channel=""
        for temp in data:
            i=i+1
            if phy_test_tssi_0.decode("utf-8")[:-1] in temp:
                tssi_0.append(data[i])
            elif phy_test_tssi_1.decode("utf-8")[:-1] in temp:
                tssi_1.append(data[i])
            elif phy_test_tssi_2.decode("utf-8")[:-1] in temp:
                tssi_2.append(data[i])
            elif phy_test_idletssi_0.decode("utf-8")[:-1] in temp:
                idletssi_0.append(data[i])
            elif phy_test_idletssi_1.decode("utf-8")[:-1] in temp:
                idletssi_1.append(data[i])
            elif phy_test_idletssi_2.decode("utf-8")[:-1] in temp:
                idletssi_2.append(data[i])
            elif getenv0.decode("utf-8")[:-1] in temp:
                pa5ga0=data[i].split(',')
            elif getenv1.decode("utf-8")[:-1] in temp:
                pa5ga1=data[i].split(',')
            elif getenv2.decode("utf-8")[:-1] in temp:
                pa5ga2=data[i].split(',')
            elif "Channel:" in temp:
                tmp = temp.split(' ')
                for ch in tmp:
                    if "Channel:" in ch:
                        channel=ch.split(":")[1]
        
        adjtssi_0=[]
        adjtssi_1=[]
        adjtssi_2=[]
        ant0=[]
        ant1=[]
        ant2=[]
        i = 0
        while i < len(tssi_0):
            try:
                x0=float(idletssi_0[i])-float(tssi_0[i])+1023
                y0=float(x0)/8
                x1=float(idletssi_1[i])-float(tssi_1[i])+1023
                y1=float(x1)/8
                x2=float(idletssi_2[i])-float(tssi_2[i])+1023
                y2=float(x2)/8
                adjtssi_0.append(y0)
                adjtssi_1.append(y1)
                adjtssi_2.append(y2)
            except ValueError:
                print("error on line",i)
            time.sleep(0.01)
            i += 1 
    
        if 36 <= int(channel) <= 44:
            a1=float(self.s16(int(pa5ga0[0],16)))/2**15
            b0=float(self.s16(int(pa5ga0[1],16)))/2**8
            b1=float(self.s16(int(pa5ga0[2],16)))/2**12
            i = 0
            while i < len(adjtssi_0): 
                ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                i=i+1
    
        elif 48 <= int(channel) <= 64:   
            a1=float(self.s16(int(pa5ga0[3],16)))/2**15
            b0=float(self.s16(int(pa5ga0[4],16)))/2**8
            b1=float(self.s16(int(pa5ga0[5],16)))/2**12
            i = 0
            while i < len(adjtssi_0): 
                ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                i=i+1
    
        elif 96 <= int(channel) <= 140:   
            a1=float(self.s16(int(pa5ga0[6],16)))/2**15
            b0=float(self.s16(int(pa5ga0[7],16)))/2**8
            b1=float(self.s16(int(pa5ga0[8],16)))/2**12
            i = 0
            while i < len(adjtssi_0): 
                ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                i=i+1
    
        elif 142 <= int(channel) <= 165:   
            a1=float(self.s16(int(pa5ga0[9],16)))/2**15
            b0=float(self.s16(int(pa5ga0[10],16)))/2**8
            b1=float(self.s16(int(pa5ga0[11],16)))/2**12
            i = 0
            while i < len(adjtssi_0): 
                ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                i=i+1
        antenna=[]
        antenna.append(ant0)
        antenna.append(ant1)
        antenna.append(ant2)
        return antenna

samet = WlUtility("192.168.2.254","root","")
print(samet.telnetGetWlData(b"wl -i wl1 phy_rssi_ant\n", 5, 0.1))
print(samet.telnetAllTssiWlDataBCM4360(1000)[0])
