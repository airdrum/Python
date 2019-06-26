import telnetlib
import sys,os
import time
import re 
import datetime
from statistics import mean , stdev

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
    def telnetExit(self):
        self.telnet.write(b"exit\n")
        print("Connection from " + self.host + " is closed.")
        

samet = WlUtility("192.168.1.65","root","")        
retval= samet.telnetGetWlData("wl -i wl1 rate; wl -i wl1 nrate\n",3,0.5)
print(retval)