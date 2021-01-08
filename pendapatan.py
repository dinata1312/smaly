import pymysql
import os

from getpass import getpass
from datetime import datetime

class Pendapatan():

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
