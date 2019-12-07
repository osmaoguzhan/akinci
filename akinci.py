import argparse
from model import portScanner

def createBanner():
    print('\033[91m'+"=================================================")
    print('\033[91m'+" ______   _    __ _____  ______   ______ _____\n"
          '\033[91m'+"| |  | | | |  / /  | |  | |  \ \ | |      | | \n"
          '\033[91m'+"| |__| | | |-< <   | |  | |  | | | |      | | \n"
          '\033[91m'+"|_|  |_| |_|  \_\ _|_|_ |_|  |_| |_|____ _|_|_\n")
    print('\033[91m'+"================================================="+'\033[0m')

def showUsage():
    print("USAGE: python3 akinci.py")

if __name__ == '__main__':
    createBanner()
    showUsage()



