from model import networkScanner
import argparse


def argParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', "--port", required=False,
                        help="Specific Port Ex: < -p 80 >\nPort Range Ex: < -p 22-45 >\nFor All Ports Ex < -p -1 >\nAs a default option it'll scan all ports",
                        default="-1",
                        action="store")
    args = parser.parse_args()
    networkScanner.networkScan(args.port)


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



