from netdiscover import *
disc = Discover()
print("=========================")
print("Scanning local network")
print("=========================")
print("Host IP: 192.168.1.41")
print("[+] [IP RANGE]")
list=disc.scan(ip_range="192.168.1.0/16")
for i in list:
    print(i)