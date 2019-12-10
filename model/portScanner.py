import nmap


class portScanner:

    def __init__(self, ip, port):
        self.portScan = nmap.PortScanner()
        self.getRange(ip, port)

    def getRange(self, ip, port):
        self.portScan.scan(ip, port)
        self.scanPorts()

    def scanPorts(self):
        for host in self.portScan.all_hosts():
            print('State : %s' % self.portScan[host].state())
            for proto in self.portScan[host].all_protocols():
                print('Protocol : %s' % proto)
                lport = self.portScan[host][proto].keys()
                for port in lport:
                    print('port : %s\tstate : %s' % (port, self.portScan[host][proto][port]['state']))
