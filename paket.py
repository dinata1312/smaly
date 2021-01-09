import pymysql
import os

from main import Menu

from getpass import getpass
from datetime import datetime

class Paket():

    def __init__(self):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()
        self.__idPaket  = ''

    # Overiding (?)
    # View Paket
    def viewPaket(self):
        
        getData     = "SELECT * FROM paket ORDER BY idPaket ASC;"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()
        return list(data)

    # Insert Paket
    def insert(self, namaPaket, harga, jenis, durasi):

        # verifyNamaPaket
        getSimiliarName = "SELECT * from `paket` WHERE `namaPaket` like '%" + str(namaPaket) + "%';"
        
        self.cursor.execute(getSimiliarName)
        data = self.cursor.fetchall()

        if len(data) > 0:
            return False

        else:
            insertPaket = "INSERT INTO `paket` (`idPaket`, `namaPaket`, `harga`, `jenis`, `durasi`) VALUES (NULL, '" + str(namaPaket) + "', '" + str(harga) + "', '" + str(jenis) + "', '" + str(durasi) + "') ;"

            # executing the quires
            self.cursor.execute(insertPaket)
            self.connection.commit()    

            return True
    
    def delete(self, idPaket):
        
        delPaket = "DELETE FROM paket WHERE idPaket = " + idPaket

        # executing the quires
        self.cursor.execute(delPaket)
        self.connection.commit()    

        return True
