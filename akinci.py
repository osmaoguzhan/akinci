
from model import networkScanner
import argparse
from controller import dbOp as db



def argParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', "--port", required=False,
                        help="Specific Port Ex: <-p 80>\nPort Range Ex: <-p 22-45>\nFor All Ports Ex <-p all>\n"
                             "For Common Ports Ex <-p common>\n")
    parser.add_argument('-d', "--db", required=False,
                        help="1: MAC\n 2:IP Address\n 3: Host IP\n4: All")
    args = parser.parse_args()

    if args.port != None:
        networkScanner.networkScan(args.port)
    elif args.db != None:
        if args.db == "1":
            mac = input("Please type the MAC you'd like to search on DB:")
            if len(mac) > 0:
                db.selectstar(str(mac),"mac")
            else:
                print("No written MAC!!")
        elif args.db == "2":
            ip = input("Please type the IP Address you'd like to search on DB:")
            if len(ip) > 0:
                db.selectstar(str(ip),"ip")
            else:
                print("Pls type an IP!!")
        elif args.db == "3":
            hostIP = input("Please type the Host IP you'd like to search on DB:")
            if len(hostIP) > 0:
                db.selectstar(str(hostIP), "hostip")
            else:
                print("No written Host IP!!")
        elif args.db == "4":
            db.getalldata()
        else:
            print("Wrong option!!")
    else:
        print("No arguments!!")



def createBanner():
    print('\033[91m'+"=================================================")
    print('\033[91m'+" ______   _    __ _____  ______   ______ _____\n"
          '\033[91m'+"| |  | | | |  / /  | |  | |  \ \ | |      | | \n"
          '\033[91m'+"| |__| | | |-< <   | |  | |  | | | |      | | \n"
          '\033[91m'+"|_|  |_| |_|  \_\ _|_|_ |_|  |_| |_|____ _|_|_\n")
    print('\033[91m'+"================================================="+'\033[0m')


if __name__ == '__main__':
    createBanner()
    argParse()



