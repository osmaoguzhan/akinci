import os
import socket
from mac_vendor_lookup import MacLookup

def defaultInfo():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    gateway = gw[2]
    host = socket.gethostname()
    try:
        print(socket.gethostbyaddr('192.168.1.1')[0])
    except:
        print("Ad bulunamadı")
    return ipaddr
    print ("IP:", ipaddr, " GW:", gateway, " Host:", host)
print(MacLookup().lookup("d8:8f:76:53:0d"))

print(defaultInfo())
