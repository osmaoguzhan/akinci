import os

a=os.popen("arp -a | awk '{print $2}'").read()
"""for ip in a:
    print(a)
    if "(" and ")" in ip:
        str(ip).replace("(","")
        str(ip).replace(")","")"""
print(a)