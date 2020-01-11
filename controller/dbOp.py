import sqlite3
from datetime import datetime
from sqlite3 import Error
import os

def createTable():
    control = 1
    if os.path.exists('info.db'):
        return control
    else:
        try:
            print("VERİTABANI OLUŞTURULUYOR")
            connection = sqlite3.connect('info.db')
            cursor = connection.cursor()
            query = "Create table if not exists allInfo (" \
                    "hostip varchar (32)," \
                    "mac varchar(32), " \
                    "ip varchar(32)," \
                    "vendor TEXT," \
                    "tcpPorts TEXT, " \
                    "udpPorts TEXT," \
                    "dateOfCon date" \
                    ")"
            cursor.execute(query)
            connection.commit()
            connection.close()
            control = 0
        except Error as e:
            control = -1
        finally:
            connection.close()
            return control

def insertinto(hostip, mac, ip, vendor, tcpPorts, udpPorts):
    if createTable() == 1 or createTable() == 0:
        connection = sqlite3.connect('info.db')
        cursor = connection.cursor()
        if len(tcpPorts) != 0:
            tcpPorts = ','.join([str(elem) for elem in tcpPorts])
        else:
            tcpPorts = ""
        if len(udpPorts) != 0:
            udpPorts = ','.join([str(elem) for elem in udpPorts])
        else:
            udpPorts = " "
        query = "INSERT INTO allInfo VALUES('" +hostip+"','"+ mac + "','" + ip + "','"+ vendor + "','" \
                + tcpPorts + "','" + udpPorts +"','"+str(datetime.now())[:16] + "')"
        try:
            cursor.execute(query)
            connection.commit()
        except:
            print("Got an error while inserting datas into db")
        finally:
            connection.close()
    elif createTable() == -1:
        print("Got an error!!")

def selectstar(mac):
    connection = sqlite3.connect('info.db')
    try:

        cursor = connection.cursor()
        query = "SELECT * FROM allInfo where mac = '" + str(mac) + "'"
        info = cursor.execute(query).fetchall()
        connection.commit()
    except Error as e:
        print(e)
        return False

    return info

def getalldata():
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    query = "Select * from allInfo"
    allData = cursor.execute(query).fetchall()
    datas = []
    for row in allData:
        datas.append(row)
    connection.commit()
    connection.close()
    return datas

a=getalldata()
print(a)