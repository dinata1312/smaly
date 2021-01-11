import pymysql
import os

import transaksi as TransaksiController

from getpass import getpass
from datetime import datetime

class Pendapatan(TransaksiController.Transaksi):

    def __init__(self):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()
    
    def byBulan(self, bulan, tahun):

        query = "SELECT * FROM transaksi WHERE `Mulai` LIKE '" + str(tahun) + "-" + str(bulan) + "%' ;"
        # print(query)
        # exit()
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        
        return data
