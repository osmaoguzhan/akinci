from netdiscover import *
from model import portScanner
from model import getInfo
from mac_vendor_lookup import MacLookup

class networkScan:
    def __init__(self, port):
        self.findBase()

        self.netScan(port)

    def netScan(self, port):
        deviceScanner = Discover()
        print("=================================")
        print("Scanning local network and ports")
        print("=================================")
        print("Host IP: " + str(self.hostIP))
        ipRange = self.ipBase+"/16"
        print("[+] IP RANGE [" + str(ipRange) + "]")
        try:
            allDevices = deviceScanner.scan(ip_range=ipRange)
        except:
            print("Got error while getting IP Addresses!")
        for device in allDevices:
            print(device['ip'].decode('ASCII'))
            try:
                print(device['mac'].decode('ASCII'))
                print(MacLookup().lookup(device['mac'].decode('ASCII')))
            except:
                print("Got error while getting vendor!")
            portScanner.portScanner(device['ip'].decode('ASCII'),port)
            print("++++++++++++++++++++++++++++++++++++++")

    def findBase(self):
        self.hostIP = getInfo.defaultInfo()
        removeLast = self.hostIP .rfind('.')
        self.ipBase = self.hostIP[:removeLast]+'.0'
        return self.ipBase
