import os
list=os.popen("nmap -sn 192.168.1.0/24 | grep MAC | awk '{print $3}'")
for i in list:
    print(i)