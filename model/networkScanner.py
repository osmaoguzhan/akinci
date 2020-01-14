from model import portScanner
from model import getInfo
import plotly.graph_objects
from controller import dbOp as db
import nmap
scanner = nmap.PortScanner()

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
        print("Scanning local network and ports")
        print('\033[91m'+"================================================="+'\033[0m')
        print("Host IP: " + str(self.hostIP))
        ipRange = self.ipBase+"/24"
        print("[+] IP RANGE [" + str(ipRange) + "]")
        print('\033[91m'+"================================================="+'\033[0m')
        try:
            a = scanner.scan(hosts=ipRange, arguments='-sP')
            for keys, value in a['scan'].items():
                if str(value['status']['state']) == 'up':
                    if self.hostIP != str(value['addresses']['ipv4']):
                        ipAddr.append(str(value['addresses']['ipv4']))
                        try:
                            if 'mac' in value['addresses'].keys():
                                mac.append(str(value['addresses']['mac']))
                                try:
                                    if 'vendor'in value.keys():
                                        if len(value['vendor']) != 0:
                                            macVendor.append(value['vendor'][value['addresses']['mac']])
                                        else:
                                            macVendor.append("None")
                                except:
                                    print("Got an error while getting MAC Vendors!!")
                            else:
                                mac.append("None")
                        except:
                            print("Got an error while getting MACs!!")
            for ip in ipAddr:

                try:
                    open.append(portScanner.portScanner(ip,port))
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
        self.hostIP = getInfo.hostIP()
        nslookup = getInfo.defaultInfo()
        removeLast = nslookup .rfind('.')
        self.ipBase = nslookup[:removeLast]+'.0'
        return self.ipBase


    def createTable(self, ipAddr, mac, macVendor, tcpPorts, udpPorts):
        fig = plotly.graph_objects.Figure(data=[plotly.graph_objects.Table(header=dict(values=['IP Address', 'MAC' , 'MAC Vendor', 'TCP Ports', 'UDP Ports']),
                                                                           cells=dict(values=[ipAddr, mac, macVendor, tcpPorts, udpPorts]))],
                                          layout_title_text="AKINCI is the tool for auto-scan local network<br>If the mac address field is empty, the machine might be a VM.")
        fig.show()

