import argparse
from model import portScanner
def argumentParse():
    argumentForTool= argparse.ArgumentParser()
    argumentForProccess=argparse.ArgumentParser()
    #argumentForTool.add_argument('-h', "--help", required=False,help="Show basic help message and exit")
    argumentForTool.add_argument('-i', "--ip", required=True, help="ip or ip range")
    argumentForTool.add_argument('-p', '--port', required=True, help="You can give just 1 port or a range. For all ports use : -p/--port -1")
    args = vars(argumentForTool.parse_args())
    portScanner.portScanner(str(args['ip']),str(args['port']))

def createBanner():
    print('\033[91m'+"=================================================")
    print('\033[91m'+" ______   _    __ _____  ______   ______ _____\n"
          '\033[91m'+"| |  | | | |  / /  | |  | |  \ \ | |      | | \n"
          '\033[91m'+"| |__| | | |-< <   | |  | |  | | | |      | | \n"
          '\033[91m'+"|_|  |_| |_|  \_\ _|_|_ |_|  |_| |_|____ _|_|_\n")
    print('\033[91m'+"================================================="+'\033[0m')
def showTools():
    print("Tools:")
    print("Name: portscanner")
    print("Example usage: akinci.py -t/--tool portscanner -i [ip or ip range] -p [port or port range]")
    print("Name: networkscanner")
    print("Example usage: akinci.py -t/--tool networkscanner -i [ip or ip range]")

if __name__ == '__main__':
    createBanner()
    argumentParse()

