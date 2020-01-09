import sqlite3
from datetime import datetime
from sqlite3 import Error
import os

class dbOperations():
    def createTable(self):
        if os.path.exists('info.db'):
            return 1
        else:
            try:
                connection = sqlite3.connect('info.db')
                cursor = connection.cursor()
                query = "Create table if not exists allInfo (mac varchar(32), ip varchar(32),ports TEXT, dateOfCon date)"
                cursor.execute(query)
                connection.commit()
                connection.close()
                return 0
            except Error as e:
                return -1

    def insertinto(self, mac, ip, ports):
        if dbOperations.createTable(self) == 1 or dbOperations.createTable(self) == 0:
            connection = sqlite3.connect('info.db')
            cursor = connection.cursor()
            control = 0
            query = "INSERT INTO allInfo VALUES('" + mac + "','" + ip + "','" + ports + "','" + str(datetime.now())[:16] + "')"
            try:
                cursor.execute(query)
                connection.commit()
                control = 1
            except:
                control = -1
            finally:
                connection.close()
                return control
        elif dbOperations.createTable(self) == -1:
            print("Got an error!!")

    def selectstar(self,mac):
        connection = sqlite3.connect('info.db')
        try:

            cursor = connection.cursor()
            query = "SELECT * FROM allInfo where mac = '" + str(mac) + "'"
            info = cursor.execute(query).fetchall()

            #mac = info[0][0]
            #ip = info[0][1]
            #ports = info[0][2]
            #date = info[0][3]
            connection.commit()
        except Error as e:
            print(e)
            return False

        return info #mac, ip, ports, date

    def getalldata(self):
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
#dbOperations.insertinto(1,"c4:6e:1f:ec:19:95","192.168.1.1","80")
a=dbOperations.selectstar(4,"c4:6e:1f:ec:19:95")
#a=dbOperations.getalldata(1)
for data in a:
    for datas in data:
        print(datas)
print(a)