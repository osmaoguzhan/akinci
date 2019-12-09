import argparse
from mac_vendor_lookup import MacLookup
def showtop20(a,ip):
    if a == str(-1):
        print("Scanning All Ports")
        print(ip)
    print("{0}".format(a))

parser = argparse.ArgumentParser()
parser.add_argument('-p',"--port", required=False ,
                    help="Specific Port Ex: <-p 80>\nPort Range Ex: <-p 22-45>\nFor All Ports Ex <-p -1>\nAs a default option it'll scan all ports",
                    default="-1",
                    type=showtop20('10.2.2.2'),
                    action="store")
args = parser.parse_args()
#print(MacLookup().lookup("d8:8f:76:53:0d"))
