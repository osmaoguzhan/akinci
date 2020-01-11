from netdiscover import *
from model import portScanner
from model import getInfo
from mac_vendor_lookup import MacLookup
import plotly.graph_objects
from controller import dbOp as db

class networkScan:

    def __init__(self, port):
        self.findBase()
        self.netScan(port)


    def netScan(self, port):
        open = []
        tcpPorts = []
        udpPorts = []
        mac = []
        macVendor = []
        ipAddr = []
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
                ipAddr.append(device['ip'].decode('ASCII'))
                try:
                    mac.append(device['mac'].decode('ASCII'))
                    macVendor.append(MacLookup().lookup(device['mac'].decode('ASCII')))
                except:
                    macVendor.append("None")
                try:
                    open.append(portScanner.portScanner(device['ip'].decode('ASCII'), port))
                except:
                    print("While scanning ports , got an error!")
            try:
                for i in range(len(open)):
                    tcpPorts.append(open[i].opentcp)
                    udpPorts.append(open[i].openudp)
                for i in range(len(mac)):
                    db.insertinto(
                        self.hostIP,
                        mac[i],
                        ipAddr[i],
                        macVendor[i],
                        tcpPorts[i],
                        udpPorts[i]
                        )
                self.createTable(ipAddr, mac, macVendor, tcpPorts, udpPorts)
            except:
                print("Got an error while creating table")

        except:
            print("Got error while getting IP Addresses!")



    def findBase(self):
        self.hostIP = getInfo.defaultInfo()
        removeLast = self.hostIP .rfind('.')
        self.ipBase = self.hostIP[:removeLast]+'.0'
        return self.ipBase


    def createTable(self, ipAddr, mac, macVendor, tcpPorts, udpPorts):
        fig = plotly.graph_objects.Figure(data=[plotly.graph_objects.Table(header=dict(values=['IP Address', 'MAC' , 'MAC Vendor', 'TCP Ports', 'UDP Ports']),
                                                                           cells=dict(values=[ipAddr, mac, macVendor, tcpPorts, udpPorts]))],
                                          layout_title_text="AKINCI is the tool for auto-scan local network")
        fig.show()

