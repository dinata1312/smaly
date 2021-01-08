import pymysql
import os

from getpass import getpass
from datetime import datetime

class CekStatus:
    def __init__(self):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()
        self.__idTransaksi  = ''
    
    def viewIDTransaksi(self):
        
        getData     = "SELECT idTransaksi FROM transaksi"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()
        
        return list(data)
        
    # View Status
    def viewStatus(self, answer):
        
        getData     = "SELECT * FROM transaksi WHERE `idTransaksi` = " + answer + ";"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()
        # print(data)
        return list(data)
