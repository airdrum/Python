
import telnetlib
import sys
import time
import re 
HOST = "192.168.2.254"
user = 'root'
password = ''

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
i=0
while i<5:
    tn.write(b"wl -i wl1 phy_rssi_ant\r\n")
    time.sleep(0.1)
    i+=1
    
tn.write(b"exit\n")

print(tn.read_all().decode('ascii').replace('\n',''))

