
import telnetlib
import sys,os
import time
import re 
import datetime

from statistics import mean , stdev



antenna_power_0=""
antenna_power_1=""
antenna_power_2=""

class WlUtility:
        # Initializer / Instance Attributes
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.telnet = telnetlib.Telnet(self.host)
        self.telnet.read_until(b"login: ")
        self.telnet.write(self.user.encode('ascii') + b"\n")
        if self.password:
            self.telnet.read_until(b"Password: ")
            self.telnet.write(self.password.encode('ascii') + b"\n")
    
    def transmitTryBCM4366(self, power_level, mean_count):
        channel=36
        bw=20
        chain=0
        powerLevelCmd = ("wl -i wl1 txpwr1 -q -o " + str(power_level*4) + "\n").encode()
        chbw_cmd = ("wl -i wl1 chanspec " + str(channel) +"/" + str(bw) +"\n").encode()
        #print("--> START Tx for " +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level))
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(b"wl -i wl1 mpc 0\n")
        self.telnet.write(b"wl -i wl1 legacylink 1\n")
        self.telnet.write(b"wl -i wl1 ssid \"\"\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 country ALL\n")
        self.telnet.write(b"wl -i wl1 wsec 0\n")
        self.telnet.write(b"wl -i wl1 stbc_rx 1\n")
        self.telnet.write(b"wl -i wl1 scansuppress 1\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 band auto\n")
        self.telnet.write(b"wl -i wl1 txbf 0\n")
        self.telnet.write(b"wl -i wl1 spect 0\n")
        self.telnet.write(b"wl -i wl1 ibss_gmode -1\n")
        self.telnet.write(b"wl -i wl1 bw_cap 5g 255\n")
        self.telnet.write(b"wl -i wl1 bw_cap 2g 3\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 mbss 0\n")
        self.telnet.write(b"wl -i wl1 frameburst 0\n")
        self.telnet.write(b"wl -i wl1 ampdu 0\n")
        self.telnet.write(b"wl -i wl1 gmode auto\n")
        self.telnet.write(b"wl -i wl1 up\n")
        self.telnet.write(b"wl -i wl1 PM 0\n")
        self.telnet.write(b"wl -i wl1 stbc_tx 0\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 bi 65535\n")
        self.telnet.write(b"wl -i wl1 mimo_txbw -1\n")
        self.telnet.write(b"wl -i wl1 2g_rate auto\n")
        self.telnet.write(b"wl -i wl1 5g_rate auto\n")
        self.telnet.write(b"wl -i wl1 ampdu 1\n")
        self.telnet.write(b"wl -i wl1 frameburst 1\n")
        self.telnet.write(b"wl -i wl1 txchain 15\n")
        self.telnet.write(b"wl -i wl1 rxchain 15\n")
        self.telnet.write(b"wl -i wl1 spatial_policy 1\n")
        if chain == 0:
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 1\n")
        elif chain == 1: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 2\n")
        elif chain == 2: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 4\n")
        elif chain == 3: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 8\n")
        self.telnet.write(b"wl -i wl1 phy_watchdog 0\n")
        self.telnet.write(b"wl -i wl1 band a\n")
        self.telnet.write(b"wl -i wl1 vht_features 3\n")
        self.telnet.write(chbw_cmd)
        self.telnet.write(b"wl -i wl1 up\n")
        self.telnet.write(b"wl -i wl1 phy_forcecal 1\n")
        self.telnet.write(("wl -i wl1 5g_rate -v 0 -s 1 --ldpc -b " + str(bw) +"\n").encode())
        self.telnet.write(b"wl -i wl1 phy_txpwrctrl 1\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop rx\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(powerLevelCmd)
        self.telnet.write(b"wl -i wl1 phy_forcecal 1\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop rx\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(b"wl -i wl1 interference_override 0\n")
        self.telnet.write(b"wl -i wl1 pkteng_start 00:11:22:33:44:55 tx 30 1500 0 88:41:FC:C3:49:0B\n")
        time.sleep(0.5)
        while True:
            try:
                samet=self.telnetTryBCM4366(mean_count)
            except ValueError:
                continue
            break
        
        
        mean_val = mean(samet)
        std_val = stdev(samet)
        print("CH" +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level) + " Mean: " + str(round(mean_val,3)) + " STD: " + str(round(std_val,3)))

        time.sleep(1)
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")       
        time.sleep(1)
        return round(mean_val,3)
    
     
    
    
    def transmitTryBCM4360(self, power_level, mean_count):
        channel=36
        bw=80
        chain=0
        powerLevelCmd = ("wl -i wl1 txpwr1 -q -o " + str(power_level*4) + "\n").encode()
        chbw_cmd = ("wl -i wl1 chanspec " + str(channel) +"/" + str(bw) +"\n").encode()
        #print("--> START Tx for " +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level))
        self.telnet.write(b"wl -i wl1 mpc 0\n")
        self.telnet.write(b"wl -i wl1 legacylink 1\n")
        self.telnet.write(b"wl -i wl1 ssid \"\"\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 country ALL\n")
        self.telnet.write(b"wl -i wl1 wsec 0\n")
        self.telnet.write(b"wl -i wl1 stbc_rx 1\n")
        self.telnet.write(b"wl -i wl1 scansuppress 1\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 band auto\n")
        self.telnet.write(b"wl -i wl1 txbf 0\n")
        self.telnet.write(b"wl -i wl1 spect 0\n")
        self.telnet.write(b"wl -i wl1 ibss_gmode -1\n")
        self.telnet.write(b"wl -i wl1 bw_cap 5g 255\n")
        self.telnet.write(b"wl -i wl1 bw_cap 2g 3\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 mbss 0\n")
        self.telnet.write(b"wl -i wl1 frameburst 0\n")
        self.telnet.write(b"wl -i wl1 ampdu 0\n")
        self.telnet.write(b"wl -i wl1 gmode auto\n")
        self.telnet.write(b"wl -i wl1 up\n")
        self.telnet.write(b"wl -i wl1 PM 0\n")
        self.telnet.write(b"wl -i wl1 stbc_tx 0\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 bi 65535\n")
        self.telnet.write(b"wl -i wl1 mimo_txbw -1\n")
        self.telnet.write(b"wl -i wl1 2g_rate auto\n")
        self.telnet.write(b"wl -i wl1 5g_rate auto\n")
        self.telnet.write(b"wl -i wl1 ampdu 1\n")
        self.telnet.write(b"wl -i wl1 frameburst 1\n")
        self.telnet.write(b"wl -i wl1 txchain 7\n")
        self.telnet.write(b"wl -i wl1 rxchain 7\n")
        self.telnet.write(b"wl -i wl1 spatial_policy 1\n")
        if chain == 0:
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 1\n")
        elif chain == 1: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 2\n")
        elif chain == 2: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 4\n")
        self.telnet.write(b"wl -i wl1 phy_watchdog 0\n")
        self.telnet.write(b"wl -i wl1 band a\n")
        self.telnet.write(b"wl -i wl1 vht_features 3\n")
        self.telnet.write(chbw_cmd)
        self.telnet.write(b"wl -i wl1 up\n")
        self.telnet.write(b"wl -i wl1 phy_forcecal 1\n")
        self.telnet.write(("wl -i wl1 5g_rate -v 0 -s 1 --ldpc -b " + str(bw) +"\n").encode())
        self.telnet.write(b"wl -i wl1 phy_txpwrctrl 1\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop rx\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(powerLevelCmd)
        self.telnet.write(b"wl -i wl1 phy_forcecal 1\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop rx\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(b"wl -i wl1 interference_override 0\n")
        self.telnet.write(b"wl -i wl1 pkteng_start 00:11:22:33:44:55 tx 30 1500 0 88:41:FC:C3:49:0B\n")
        time.sleep(0.5)
        while True:
            try:
                samet=self.telnetTryBCM4360(mean_count)
            except ValueError:
                continue
            break
        
        
        mean_val = mean(samet)
        std_val = stdev(samet)
        print("CH" +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level) + " Mean: " + str(round(mean_val,3)) + " STD: " + str(round(std_val,3)))

        time.sleep(1)
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")       
        time.sleep(1)
        return round(mean_val,3)
    
     


    def transmitPowerBCM4360(self, channel, bw, chain, power_level, mean_count):
        
        powerLevelCmd = ("wl -i wl1 txpwr1 -q -o " + str(power_level*4) + "\n").encode()
        chbw_cmd = ("wl -i wl1 chanspec " + str(channel) +"/" + str(bw) +"\n").encode()
        #print("--> START Tx for " +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level))
        self.telnet.write(b"wl -i wl1 mpc 0\n")
        self.telnet.write(b"wl -i wl1 legacylink 1\n")
        self.telnet.write(b"wl -i wl1 ssid \"\"\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 country ALL\n")
        self.telnet.write(b"wl -i wl1 wsec 0\n")
        self.telnet.write(b"wl -i wl1 stbc_rx 1\n")
        self.telnet.write(b"wl -i wl1 scansuppress 1\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 band auto\n")
        self.telnet.write(b"wl -i wl1 txbf 0\n")
        self.telnet.write(b"wl -i wl1 spect 0\n")
        self.telnet.write(b"wl -i wl1 ibss_gmode -1\n")
        self.telnet.write(b"wl -i wl1 bw_cap 5g 255\n")
        self.telnet.write(b"wl -i wl1 bw_cap 2g 3\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 mbss 0\n")
        self.telnet.write(b"wl -i wl1 frameburst 0\n")
        self.telnet.write(b"wl -i wl1 ampdu 0\n")
        self.telnet.write(b"wl -i wl1 gmode auto\n")
        self.telnet.write(b"wl -i wl1 up\n")
        self.telnet.write(b"wl -i wl1 PM 0\n")
        self.telnet.write(b"wl -i wl1 stbc_tx 0\n")
        self.telnet.write(b"wl -i wl1 down\n")
        self.telnet.write(b"wl -i wl1 bi 65535\n")
        self.telnet.write(b"wl -i wl1 mimo_txbw -1\n")
        self.telnet.write(b"wl -i wl1 2g_rate auto\n")
        self.telnet.write(b"wl -i wl1 5g_rate auto\n")
        self.telnet.write(b"wl -i wl1 ampdu 1\n")
        self.telnet.write(b"wl -i wl1 frameburst 1\n")
        self.telnet.write(b"wl -i wl1 txchain 7\n")
        self.telnet.write(b"wl -i wl1 rxchain 7\n")
        self.telnet.write(b"wl -i wl1 spatial_policy 1\n")
        if chain == 0:
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 1\n")
        elif chain == 1: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 2\n")
        elif chain == 2: 
            self.telnet.write(b"wl -i wl1 txcore -s 1 -c 4\n")
        self.telnet.write(b"wl -i wl1 phy_watchdog 0\n")
        self.telnet.write(b"wl -i wl1 band a\n")
        self.telnet.write(b"wl -i wl1 vht_features 3\n")
        self.telnet.write(chbw_cmd)
        self.telnet.write(b"wl -i wl1 up\n")
        self.telnet.write(b"wl -i wl1 phy_forcecal 1\n")
        self.telnet.write(("wl -i wl1 5g_rate -v 0 -s 1 --ldpc -b " + str(bw) +"\n").encode())
        self.telnet.write(b"wl -i wl1 phy_txpwrctrl 1\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop rx\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(powerLevelCmd)
        self.telnet.write(b"wl -i wl1 phy_forcecal 1\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop rx\n")
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")
        self.telnet.write(b"wl -i wl1 interference_override 0\n")
        self.telnet.write(b"wl -i wl1 pkteng_start 00:11:22:33:44:55 tx 30 1500 0 88:41:FC:C3:49:0B\n")
        time.sleep(0.5)
        while True:
            try:
                samet=self.telnetAllTssiWlDataBCM4360(mean_count,channel,chain)
            except ValueError:
                continue
            break
        
        
        mean_val = mean(samet)
        std_val = stdev(samet)
        print("CH" +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level) + " Mean: " + str(round(mean_val,3)) + " STD: " + str(round(std_val,3)))


        #        print("--> STOP Tx for " +str(channel)+"/"+str(bw) + " - Chain: " +str(chain) + " - Powerlevel: " + str(power_level))
        time.sleep(1)
        self.telnet.write(b"wl -i wl1 pkteng_stop tx\n")       
        time.sleep(1)
        return round(mean_val,3)
    
      
    def telnetGetWlData(self,key,count,sleep_time):
        
        i=0
    
        while i<count:
            self.telnet.write((key + "\n").encode())
            time.sleep(sleep_time)
            i+=1
        #self.telnet.write(b"exit\n")
        
        output = self.telnet.read_very_eager().decode('ascii')
        #print(output)
        data = output.split('\r')
        
        i=0
               
        my_list = []
        i=0
        for temp in data:
            i=i+1
            my_list.append(temp)
        return my_list
    
    def telnetTryBCM4366(self,count):
        chain=0
        channel=36
        getenv0=b"env_test getenv 1:pa5ga0\n"
        phy_test_tssi_0 = b"wl -i wl1 phy_test_tssi 0\n"
        phy_test_idletssi_0 = b"wl -i wl1 phy_test_idletssi 0\n"
        
        i=0
        self.telnet.write(b"iwconfig\r\n")
        self.telnet.write(getenv0)
        while i<count:
            self.telnet.write(phy_test_tssi_0)
            self.telnet.write(phy_test_idletssi_0)
            time.sleep(0.1)
            i+=1
        output = self.telnet.read_very_eager().decode('ascii').replace('\n','')
        #print(output)
        data = output.split('\r')
        i=0
        testtssi_0 = []
        idletssi_0 = []
        pa5ga0 = ""
        samet =[]
        #channel=""
        for temp in data:
            i=i+1
            if phy_test_tssi_0.decode("utf-8")[:-1] in temp:
                testtssi_0.append(data[i])
            elif phy_test_idletssi_0.decode("utf-8")[:-1] in temp:
                idletssi_0.append(data[i])

            elif getenv0.decode("utf-8")[:-1] in temp:
                pa5ga0=data[i].split(',')
        
        
        adjtssi_0=[]
        ant0=[]
        i = 0
        #print("idletssi_0: " +str(idletssi_0))
        #print("tssi_0: " +str(testtssi_0))
        while i < len(testtssi_0):
            try:
                y0=float(idletssi_0[i])-float(testtssi_0[i])+1023
                

                adjtssi_0.append(y0)
            except IndexError:
                y0 = 'null'
            time.sleep(0.01)
            i += 1 
        if chain == 0:
            if 36 <= channel<= 44:
                A=(float(self.s16(int(pa5ga0[0],16)))/2**8)
                B=(float(self.s16(int(pa5ga0[1],16)))/2**30)
                C=(float(self.s16(int(pa5ga0[2],16)))/2**12)
                D=(float(self.s16(int(pa5ga0[3],16)))/(2**-7))
                i = 0
                while i < len(adjtssi_0): 
                    n = adjtssi_0[i]
                    ant0.append(A+B*n**2+C*n**2/(n**2-D))
                    i=i+1
        antenna=[]
        antenna.append(ant0)
        return antenna[chain]
    
    def telnetExit(self):
        self.telnet.write(b"exit\n")
        print("Connection from " + self.host + " is closed.")
        
    def s16(self,value):
        return -(value & 0x8000) | (value & 0x7fff)
    
    def telnetTryBCM4360(self,count):
        chain=0
        channel=36
        getenv0=b"env_test getenv 1:pa5ga0\n"
        phy_test_tssi_0 = b"wl -i wl1 phy_test_tssi 0\n"
        phy_test_idletssi_0 = b"wl -i wl1 phy_test_idletssi 0\n"
        txpwr1=b"wl -i wl1 txpwr1\n"
        i=0
        self.telnet.write(b"iwconfig\r\n")
        self.telnet.write(getenv0)
        while i<count:
            self.telnet.write(phy_test_tssi_0)
            self.telnet.write(phy_test_idletssi_0)
            time.sleep(0.1)
            i+=1
        output = self.telnet.read_very_eager().decode('ascii').replace('\n','')
        #print(output)
        data = output.split('\r')
        i=0
        tssi_0 = []
        idletssi_0 = []
        pa5ga0 = ""
        samet =[]
        #channel=""
        for temp in data:
            i=i+1
            if phy_test_tssi_0.decode("utf-8")[:-1] in temp:
                tssi_0.append(data[i])
            elif phy_test_idletssi_0.decode("utf-8")[:-1] in temp:
                idletssi_0.append(data[i])

            elif getenv0.decode("utf-8")[:-1] in temp:
                pa5ga0=data[i].split(',')
        
        
        adjtssi_0=[]
        ant0=[]
        i = 0
        print("idletssi_0: " +str(idletssi_0))
        print("tssi_0: " +str(tssi_0))
        while i < len(tssi_0):
            try:
                x0=float(idletssi_0[i])-float(tssi_0[i])+1023
                y0=float(x0)/8

                adjtssi_0.append(y0)
            except IndexError:
                y0 = 'null'
            time.sleep(0.01)
            i += 1 
        if chain == 0:
            if 36 <= channel<= 44:
                a1=float(self.s16(int(pa5ga0[0],16)))/2**15
                b0=float(self.s16(int(pa5ga0[1],16)))/2**8
                b1=float(self.s16(int(pa5ga0[2],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    i=i+1
        antenna=[]
        antenna.append(ant0)
        return antenna[chain]
    
    def telnetAllTssiWlDataBCM4360(self,count,channel,chain):

        phy_test_tssi_0 = b"wl -i wl1 phy_test_tssi 0\n"
        phy_test_tssi_1 = b"wl -i wl1 phy_test_tssi 1\n"
        phy_test_tssi_2 = b"wl -i wl1 phy_test_tssi 2\n"
        phy_test_idletssi_0 = b"wl -i wl1 phy_test_idletssi 0\n"
        phy_test_idletssi_1 = b"wl -i wl1 phy_test_idletssi 1\n"
        phy_test_idletssi_2 = b"wl -i wl1 phy_test_idletssi 2\n"
        getenv0=b"env_test getenv 1:pa5ga0\n"
        getenv1=b"env_test getenv 1:pa5ga1\n"
        getenv2=b"env_test getenv 1:pa5ga2\n"
        i=0
        self.telnet.write(b"iwconfig\r\n")
        self.telnet.write(getenv0)
        self.telnet.write(getenv1)
        self.telnet.write(getenv2)
        while i<count:
            self.telnet.write(phy_test_tssi_0)
            self.telnet.write(phy_test_tssi_1)
            self.telnet.write(phy_test_tssi_2)
            self.telnet.write(phy_test_idletssi_0)
            self.telnet.write(phy_test_idletssi_1)
            self.telnet.write(phy_test_idletssi_2)
            time.sleep(0.1)
            i+=1
        output = self.telnet.read_very_eager().decode('ascii').replace('\n','')
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
        #channel=""
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
            except IndexError:
                y0 = 'null'
                y1 = 'null'
                y2 = 'null'
            time.sleep(0.01)
            i += 1 
        if chain == 0:
            if 36 <= channel<= 44:
                a1=float(self.s16(int(pa5ga0[0],16)))/2**15
                b0=float(self.s16(int(pa5ga0[1],16)))/2**8
                b1=float(self.s16(int(pa5ga0[2],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 48 <= channel<= 64:   
                a1=float(self.s16(int(pa5ga0[3],16)))/2**15
                b0=float(self.s16(int(pa5ga0[4],16)))/2**8
                b1=float(self.s16(int(pa5ga0[5],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 96 <= channel<= 140:   
                a1=float(self.s16(int(pa5ga0[6],16)))/2**15
                b0=float(self.s16(int(pa5ga0[7],16)))/2**8
                b1=float(self.s16(int(pa5ga0[8],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 142 <= channel<= 165:   
                a1=float(self.s16(int(pa5ga0[9],16)))/2**15
                b0=float(self.s16(int(pa5ga0[10],16)))/2**8
                b1=float(self.s16(int(pa5ga0[11],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        elif chain == 1:
            if 36 <= channel<= 44:
                a1=float(self.s16(int(pa5ga1[0],16)))/2**15
                b0=float(self.s16(int(pa5ga1[1],16)))/2**8
                b1=float(self.s16(int(pa5ga1[2],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 48 <= channel<= 64:   
                a1=float(self.s16(int(pa5ga1[3],16)))/2**15
                b0=float(self.s16(int(pa5ga1[4],16)))/2**8
                b1=float(self.s16(int(pa5ga1[5],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 96 <= channel<= 140:   
                a1=float(self.s16(int(pa5ga1[6],16)))/2**15
                b0=float(self.s16(int(pa5ga1[7],16)))/2**8
                b1=float(self.s16(int(pa5ga1[8],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 142 <= channel<= 165:   
                a1=float(self.s16(int(pa5ga1[9],16)))/2**15
                b0=float(self.s16(int(pa5ga1[10],16)))/2**8
                b1=float(self.s16(int(pa5ga1[11],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        elif chain == 2:
            if 36 <= channel<= 44:
                a1=float(self.s16(int(pa5ga2[0],16)))/2**15
                b0=float(self.s16(int(pa5ga2[1],16)))/2**8
                b1=float(self.s16(int(pa5ga2[2],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 48 <= channel<= 64:   
                a1=float(self.s16(int(pa5ga2[3],16)))/2**15
                b0=float(self.s16(int(pa5ga2[4],16)))/2**8
                b1=float(self.s16(int(pa5ga2[5],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 96 <= channel<= 140:   
                a1=float(self.s16(int(pa5ga2[6],16)))/2**15
                b0=float(self.s16(int(pa5ga2[7],16)))/2**8
                b1=float(self.s16(int(pa5ga2[8],16)))/2**12
                i = 0
                while i < len(adjtssi_0): 
                    ant0.append((b0+(b1*adjtssi_0[i]))/(1+(a1*adjtssi_0[i])))
                    ant1.append((b0+b1*adjtssi_1[i])/(1+a1*adjtssi_1[i]))
                    ant2.append((b0+b1*adjtssi_2[i])/(1+a1*adjtssi_2[i]))
                    i=i+1
        
            elif 142 <= channel<= 165:   
                a1=float(self.s16(int(pa5ga2[9],16)))/2**15
                b0=float(self.s16(int(pa5ga2[10],16)))/2**8
                b1=float(self.s16(int(pa5ga2[11],16)))/2**12
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
        return antenna[chain]
    def telnetReboot(self):        
        i=0
        self.telnet.write(b"reboot\n")
        time.sleep(120)
        
"""samet = WlUtility("192.168.1.65","root","")        
retval= samet.telnetGetWlData("wl -i wl1 rate; wl -i wl1 nrate\n",30,0.5)

rate=[]
nrate=[]
input = sys.argv[1]
r = open("rate.txt","a+")
n = open("nrate.txt","a+")
r.write("\n"+input+" Tesla Attenuation")
n.write("\n"+input+" Tesla Attenuation")
r.write("==Rate==")
n.write("==NRate==")
for val in retval:
    if "Mbps" in val:
        
        r.write(val)
        #rate.append((val.replace("\n", "")))
    elif "vht" in val:
        n.write(val)
        #nrate.append((val.replace("\n", "")))
r.close()
n.close()"""

"""       
samet = WlUtility("192.168.2.254","root","")
channelList = [36,52,100,132,149]
chainList = [0,1,2]
bwList=[20]
power=[20.5]
i=1
rbt=0
while True:
    print("==Reboot:" + str(rbt) + " at " + str(datetime.datetime.now()))
    for ch in channelList:
        for ant in chainList:
            for bw in bwList:
                #print("===========TEST " +str(i)+" CH:" + str(ch) + "/" + str(bw) + " Ant:" + str(ant) + "==============")
                rt=0
                for pw in power:
                    while rt < 1:
                        samet.transmitPowerBCM4360(ch, bw,ant,pw,50)
                        rt = rt +1
                i=i+1
    rbt+=1
    samet.telnetReboot()
print("Overall test is finished at " + str(datetime.datetime.now()))
#CH36/20, Chain-0, TxPow=20.5, MeanCount=100
"""