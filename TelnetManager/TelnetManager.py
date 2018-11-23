
import telnetlib
import sys
import time
import re 




commandArray=[]

"""    tn.write(b"iwconfig\r\n")
    tn.write(b"env_test getenv 1:pa5ga0\r\n")
    tn.write(b"env_test getenv 1:pa5ga1\r\n")
    tn.write(b"env_test getenv 1:pa5ga2\r\n")"""

def addWlCommand(wlString):
    commandArray.append(wlString)
    
def telnetGetWlData(key,count):
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

    while i<count:
        tn.write(key)
        time.sleep(0.1)
        i+=1
    tn.write(b"exit\n")
    output = tn.read_all().decode('ascii').replace('\n','')
    #print(output)
    data = output.split('\r')
    i=0
    my_list = []
    for temp in data:
        i=i+1
        if key.decode("utf-8")[:-1] in temp:
            my_list.append(data[i])
    return my_list

def telnetAllTssiWlDataBCM4360(count):
    HOST = "192.168.2.254"
    user = 'root'
    password = ''
    phy_test_tssi_0 = b"wl -i wl1 phy_test_tssi 0\n"
    phy_test_tssi_1 = b"wl -i wl1 phy_test_tssi 1\n"
    phy_test_tssi_2 = b"wl -i wl1 phy_test_tssi 2\n"
    phy_test_idletssi_0 = b"wl -i wl1 phy_test_idletssi 0\n"
    phy_test_idletssi_1 = b"wl -i wl1 phy_test_idletssi 1\n"
    phy_test_idletssi_2 = b"wl -i wl1 phy_test_idletssi 2\n"
    getenv0=b"env_test getenv 1:pa5ga0\n"
    getenv1=b"env_test getenv 1:pa5ga1\n"
    getenv2=b"env_test getenv 1:pa5ga2\n"
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
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
    i = 0
    while i < len(tssi_0):
        adjtssi_0.append((int(idletssi_0[i])-int(tssi_0[i])+1023)/8 )
        adjtssi_1.append((int(idletssi_1[i])-int(tssi_1[i])+1023)/8 )
        adjtssi_2.append((int(idletssi_2[i])-int(tssi_2[i])+1023)/8 )
        i += 1 
    print(tssi_0)
    print(idletssi_0)
    print(adjtssi_0)  
    if 36 <= int(channel) <= 44:   
        print(pa5ga0[0:3])
        print(pa5ga1[0:3])
        print(pa5ga2[0:3])
    elif 48 <= int(channel) <= 64:   
        print(pa5ga0[3:6])
        print(pa5ga1[3:6])
        print(pa5ga2[3:6])
    elif 96 <= int(channel) <= 140:   
        print(pa5ga0[6:9])
        print(pa5ga1[6:9])
        print(pa5ga2[6:9])
    elif 142 <= int(channel) <= 165:   
        print(pa5ga0[9:12])
        print(pa5ga1[9:12])
        print(pa5ga2[9:12])
    samet.append(tssi_0)
    samet.append(tssi_1)
    samet.append(tssi_2)
    return samet

print(telnetAllTssiWlDataBCM4360(10))

