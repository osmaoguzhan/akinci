import sqlite3
from datetime import datetime
from sqlite3 import Error
import os
import plotly.graph_objects


def createTable():
    control = 1
    if os.path.exists('dbFiles/info.db'):
        return control
    else:
        try:
            connection = sqlite3.connect('dbFiles/info.db')
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
        connection = sqlite3.connect('dbFiles/info.db')
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

def selectstar(data, argsOption):
    info = []
    try:
        connection = sqlite3.connect('dbFiles/info.db')
        cursor = connection.cursor()
        query = "SELECT * FROM allInfo where " + str(argsOption) + "='" + str(data) + "'"
        info = cursor.execute(query).fetchall()
        connection.commit()
    except Error as e:
        print(e)
        info = False
    finally:
        connection.close()
        plotTable(info)


def getalldata():
    try:
        connection = sqlite3.connect('dbFiles/info.db')
        cursor = connection.cursor()
        query = "Select * from allInfo"
        allData = cursor.execute(query).fetchall()
        datas = []
        for row in allData:
            datas.append(row)
        connection.commit()
        connection.close()
    except Error as e:
        print(e)
        datas = False
    finally:
        connection.close()
        plotTable(datas)

def plotTable(datas):
    hostIP = []
    mac = []
    ipAddr = []
    macVendor= []
    tcpPorts = []
    udpPorts = []
    date= []
    if datas != False:
        for i in range(len(datas)):
            hostIP.append(datas[i][0])
            mac.append(datas[i][1])
            ipAddr.append(datas[i][2])
            macVendor.append(datas[i][3])
            tcpPorts.append(datas[i][4])
            udpPorts.append(datas[i][5])
            date.append(datas[i][6])
        fig = plotly.graph_objects.Figure(data=[plotly.graph_objects.Table(
            header=dict(values=['Host IP', 'IP Address', 'MAC' , 'MAC Vendor', 'TCP Ports', 'UDP Ports', 'Scan Date']),
            cells=dict(values=[hostIP, ipAddr, mac, macVendor, tcpPorts, udpPorts, date]))],
            layout_title_text="AKINCI is the tool for auto-scan local network")

        fig.show()
        checkPorts(tcpPorts)

    else:
        print("No data found!!")

def checkPorts(tcpPorts):
    listTcp= []
    tcpPorts = ','.join([str(elem) for elem in tcpPorts if elem != ""])
    if len(tcpPorts) != 0:
        listTcp = tcpPorts.split(",")
    listTcp = list(dict.fromkeys(listTcp))
    info = []
    ports = []
    protocol = []
    keywords = []
    print(listTcp)
    for i in range(len(listTcp)):
        try:
            connection = sqlite3.connect('dbFiles/ports.db')
            cursor = connection.cursor()
            query = "SELECT * FROM ports where port ='" + str(listTcp[i]) + "'"
            info = cursor.execute(query).fetchall()
            connection.commit()
        except Error as e:
            print(e)
            info = False
        finally:
            connection.close()

        for i in range(len(info)):
            ports.append(info[i][0])
            protocol.append(info[i][1])
            keywords.append(info[i][2])


    fig2 = plotly.graph_objects.Figure(data=[plotly.graph_objects.Table(
        header=dict(values=['Ports', 'Protocol', 'Keyword']),
        cells=dict(values=[ports, protocol, keywords]))],
        layout_title_text="Listing of Port and Protocol, with known attacks.")
    fig2.show()

