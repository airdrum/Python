'''
Created on 4 Ara 2018

@author: samet.yildiz
'''

from TelnetManager import WlUtility

if __name__ == '__main__':
    samet = WlUtility("192.168.2.254","root","")
    print(samet.telnetGetWlData("wl -i wl1 phy_rssi_ant", 3, 1))
    pass