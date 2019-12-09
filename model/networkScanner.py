from netdiscover import *
from model import portScanner
from model import getInfo


class networkScan:
    def __init__(self,port):
        self.findBase()
        #networkScan.findBase(self)
        self.netScan(port)

    def netScan(self,port):
        deviceScanner = Discover()
        print("=========================")
        print("Scanning local network")
        print("=========================")
        print("Host IP: " +str(self.hostIP))
        ipRange=self.ipBase+"/16"
        print("[+] IP RANGE [" + str(ipRange) + "]")
        allDevices=deviceScanner.scan(ip_range=ipRange)
        for device in allDevices:
            print(device['ip'].decode('ASCII'))
            portScanner.portScanner(device['ip'].decode('ASCII'),port)

    def findBase(self):
        self.hostIP = getInfo.defaultInfo()
        removeLast = self.hostIP .rfind('.')
        self.ipBase = self.hostIP [:removeLast]+'.0'
        return self.ipBase
