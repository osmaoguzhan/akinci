import nmap

class portScanner:

    def __init__(self, ip, port):
        if port == "all":
            port = "1-65535"
        elif port == "common":
            port = "1-800"
        self.main(ip, port)

    def __dict__(self):
        return self.opentcp,self.openudp

    def main(self,ip,port):
        self.portScan = nmap.PortScanner()
        self.getRange(ip, port)


    def getRange(self, ip, port):
        self.portScan.scan(ip, port)
        self.scanPorts()

    def scanPorts(self):
        self.opentcp = []
        self.openudp = []
        for host in self.portScan.all_hosts():
            for proto in self.portScan[host].all_protocols():
                lport = self.portScan[host][proto].keys()
                for port in lport:
                  if self.portScan[host][proto][port]['state'] == "open":
                      if proto == "tcp":
                          self.opentcp.append(port)
                      elif proto == "udp":
                          self.openudp.append(port)