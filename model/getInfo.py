import subprocess
import re
import socket

def defaultInfo():

    process = subprocess.Popen(["nslookup", "www.google.com"], stdout=subprocess.PIPE)
    output = process.communicate()[0].split('\n'.encode("ASCII"))

    ip_arr = []
    for data in output:
        if 'Address'.encode("ASCII") in data:
            ip_arr.append(data.replace('Address: '.encode("ASCII"), ''.encode("ASCII")))

    ip = ip_arr[0].decode("ASCII")
    ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip)
    return ip_candidates[0]


def hostIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = str(s.getsockname()[0])
    s.close()
    return ip