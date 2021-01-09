import pymysql
import os

from main import Menu

from getpass import getpass
from datetime import datetime

class Transaksi():

    def __init__(self):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()
        self.__idTransaksi   = ''
        self.__detail        = []
        self.__addDataTransaksi = { 
                                    "detail"          : [[] ],
                                    "status"          : 'belum selesai',
                                    "mulai"           : datetime.today().strftime('%Y-%m-%d')
                                  }
    
    # Menambahkan detail transaksi
    def addDetail(self, JenisCucian, berat, ke):
        
        self.__addDataTransaksi['detail'].append([])
        self.__addDataTransaksi['detail'][ke].append(JenisCucian)
        self.__addDataTransaksi['detail'][ke].append(berat)

        # print(self.__addDataTransaksi['detail'])

        return True
    
    # Menambahkan Transaksi
    def insert(self, namaPelanggan):
        
        insertTransaksi = "INSERT INTO `transaksi` (`idTransaksi`, `namaPelanggan`, `status`, `Mulai`) VALUES (NULL, '" + namaPelanggan + "', 'belum selesai', '" + self.__addDataTransaksi['mulai'] + "')"
        
        #executing the quires
        self.cursor.execute(insertTransaksi)
        self.connection.commit()

        getData     = "SELECT * FROM transaksi ORDER BY idTransaksi DESC LIMIT 1;"

        self.cursor.execute(getData)
        data = list(self.cursor.fetchall() )

        self.__addDataTransaksi['detail'].pop(len(self.__addDataTransaksi['detail']) - 1)

        insertDetail = "INSERT INTO `detailPakaian` (`idTransaksi`, `idPaket`, `berat`) VALUES" 
        value = ''

        for i in self.__addDataTransaksi['detail']:
                
            value = value + "(" + str(data[0][0]) + ", " + str(i[0]) + ", " + str(i[1]) + "),"

        insertDetail = insertDetail + value[:-1] + ";"

        # executing the quires
        self.cursor.execute(insertDetail)
        self.connection.commit()

        return True
 
    # Memperbarui Paket
    def update(self, idTransaksi):
   
        getData     = "SELECT idTransaksi FROM transaksi WHERE `idTransaksi` = " + str(idTransaksi) + "  LIMIT 1;"

        self.cursor.execute(getData)

        data = self.cursor.fetchall()

        if len(data) == 0:
            input("SALAH")
            return False
        else:
            # print(idTransaksi)
            # exit()
            updateData  = "UPDATE `transaksi` SET `status` = 'selesai' WHERE `idTransaksi` = " + str(idTransaksi)

            self.cursor.execute(updateData)
            self.connection.commit()

            return True

    # View Transaksi
    def viewTransaksi(self):
        
        getData     = "SELECT * FROM transaksi ORDER BY idTransaksi DESC LIMIT 20;"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()
        
        return list(data)

    # View Paket
    def viewPaket(self):
        
        getData     = "SELECT * FROM paket ORDER BY idPaket ASC;"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()

        return list(data)

    # Detail Transaksi
    def detailTransaksi(self, idTransaksi):

        getDetail   = "SELECT * FROM detailpakaian WHERE `idTransaksi` = " + str(idTransaksi) + ";"

        self.cursor.execute(getDetail)

        data = self.cursor.fetchall()

        return list(data)

    # Mencari Paket
    def findPaket(self, idPaket):

        getData     = "SELECT * FROM paket WHERE `idPaket` = " + str(idPaket) + "  LIMIT 1;"

        self.cursor.execute(getData)

        data = self.cursor.fetchall()
        
        return list(data)

    # kalau ga pake voucher
    # def tanpavoucher(self, namaPelanggan):

        # insertTransaksi = "INSERT INTO `transaksi` (`idTransaksi`, `namaPelanggan`, `status`, `idPotongan`, `Mulai`) VALUES (NULL, '" + namaPelanggan + "', 'belum selesai', NULL, '" + self.__addDataTransaksi['mulai'] + "')"

        # #executing the quires
        # self.cursor.execute(insertTransaksi)
        # self.connection.commit()

        # getData     = "SELECT * FROM transaksi ORDER BY idTransaksi DESC LIMIT 1;"

        # self.cursor.execute(getData)
        # data = list(self.cursor.fetchall() )

        # self.__addDataTransaksi['detail'].pop(len(self.__addDataTransaksi['detail']) - 1)

        # insertDetail = "INSERT INTO `detailPakaian` (`idTransaksi`, `idPaket`, `berat`) VALUES" 
        # value = ''

        # for i in self.__addDataTransaksi['detail']:
            
        #         # print(i[0],i[1])
        #     value = value + "(" + str(data[0][0]) + ", " + str(i[0]) + ", " + str(i[1]) + "),"
        # insertDetail = insertDetail + value[:-1] + ";"
        
        # # executing the quires
        # self.cursor.execute(insertDetail)
        # self.connection.commit()

        # return True

    # # kalau pake voucher
    # def pakevoucher(self, namaPelanggan, kodevoucher):
        
        # insertTransaksi = "INSERT INTO `transaksi` (`idTransaksi`, `namaPelanggan`, `status`, `idPotongan`, `Mulai`) VALUES (NULL, '" + namaPelanggan + "', 'belum selesai', " + kodevoucher + ", '" + self.__addDataTransaksi['mulai'] + "')"
        
        # #executing the quires
        # self.cursor.execute(insertTransaksi)
        # self.connection.commit()

        # getData     = "SELECT * FROM transaksi ORDER BY idTransaksi DESC LIMIT 1;"

        # self.cursor.execute(getData)
        # data = list(self.cursor.fetchall() )

        # self.__addDataTransaksi['detail'].pop(len(self.__addDataTransaksi['detail']) - 1)

        # insertDetail = "INSERT INTO `detailPakaian` (`idTransaksi`, `idPaket`, `berat`) VALUES" 
        # value = ''

        # for i in self.__addDataTransaksi['detail']:
                
        #     value = value + "(" + str(data[0][0]) + ", " + str(i[0]) + ", " + str(i[1]) + "),"

        # insertDetail = insertDetail + value[:-1] + ";"

        # # executing the quires
        # self.cursor.execute(insertDetail)
        # self.connection.commit()

        # return True

    # View Paket
    def viewPaket(self):
        
        getData     = "SELECT * FROM paket ORDER BY idPaket ASC;"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()

        return list(data)

    # Detail Transaksi
    def detailTransaksi(self, idTransaksi):

        getDetail   = "SELECT * FROM detailpakaian WHERE `idTransaksi` = " + str(idTransaksi) + ";"

        self.cursor.execute(getDetail)

        data = self.cursor.fetchall()

        return list(data)

    # Mencari Paket
    def findPaket(self, idPaket):

        getData     = "SELECT * FROM paket WHERE `idPaket` = " + str(idPaket) + "  LIMIT 1;"

        self.cursor.execute(getData)

        data = self.cursor.fetchall()
        
        return list(data)
