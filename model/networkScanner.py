from netdiscover import *
from model import portScanner
from model import getInfo
from mac_vendor_lookup import MacLookup

class networkScan:
    def __init__(self, port):
        self.findBase()
        self.netScan(port)

    def netScan(self, port):
        open = {}
        deviceScanner = Discover()
        print("=================================")
        print("Scanning local network and ports")
        print("=================================")
        print("Host IP: " + str(self.hostIP))
        ipRange = self.ipBase+"/16"
        print("[+] IP RANGE [" + str(ipRange) + "]")
        print("++++++++++++++++++++++++++++++++++++++")
        try:
            allDevices = deviceScanner.scan(ip_range=ipRange)
            for device in allDevices:
                ipAddr = device['ip'].decode('ASCII')
                try:
                    mac = device['mac'].decode('ASCII')
                    macVendor = MacLookup().lookup(device['mac'].decode('ASCII'))
                except:
                    macVendor = "None"

                self.open = portScanner.portScanner(device['ip'].decode('ASCII'), port)
                print("|===========================|========================|==============================|==============================|")
                print("|                           |                        |                              |                              |")
                print("|    " + str(ipAddr) + "    |    " + str(mac) + "    |    " + str(macVendor) + "    |    " + str(open.open) + "    |")
                print("|                           |                        |                              |                              |")
                print("|===========================|========================|==============================|==============================|")

        except:
            print("Got error while getting IP Addresses!")



    def findBase(self):
        self.hostIP = getInfo.defaultInfo()
        removeLast = self.hostIP .rfind('.')
        self.ipBase = self.hostIP[:removeLast]+'.0'
        return self.ipBase
