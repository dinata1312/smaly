import pymysql
import os
import main
from getpass import getpass
from datetime import datetime

conn = cursor = None
#fungsi koneksi database
def openDb():
   global conn, cursor
   conn =  pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
   cursor = conn.cursor()	

class Login:
    def __init__(self, username, password):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()
        self.__password = password
        self.__username = username
        self.__namaLengkap = ''

    @property
    def username(self):
        pass
    @username.getter
    def username(self):
        return self.__username
    @username.setter
    def username(self, input):
        self.__username = input
        
    @property
    def namaLengkap(self):
        pass
    @namaLengkap.getter
    def namaLengkap(self):
        return self.__namaLengkap
    @namaLengkap.setter
    def namaLengkap(self, input):
        self.__namaLengkap = input

    def auth(self):

        # queries for retrievint all rows
        getUser = "SELECT * FROM `users` WHERE `username` = '" + self.__username + "' AND `password` = '" + self.__password + "';"

        #executing the quires
        self.cursor.execute(getUser)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print(self.__username, self.__password)
            print('username atau password salah !')
            input('\ntekan ENTER untuk lanjut')
            main.main()
        else:
            self.__username    = rows[0][0]
            self.__namaLengkap = rows[0][2]

            #commiting the connection then closing it.
            self.connection.commit()
            self.connection.close()
            os.system('cls')
            main.menu()
            # os.system('python adminPage.py')

class Transaksi(Login):

    def __init__(self):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()
        self.__idTransaksi   = ''
        self.__detail        = []
        self.__addDataTransaksi = { 
                                    "detail"          : [[ ] ],
                                    "namaPelanggan"   : '',
                                    "status"          : 'belum selesai',
                                    "idPotongan"      : '',
                                    "mulai"           : datetime.today().strftime('%Y-%m-%d')
                                  }
    
    def addDetail(self, JenisCucian, berat, ke):
        
        self.__addDataTransaksi['detail'].append([])
        self.__addDataTransaksi['detail'][ke].append(JenisCucian)
        self.__addDataTransaksi['detail'][ke].append(berat)

        # print(self.__addDataTransaksi['detail'])

        return True
    
    def verifyVoucher(self, kode):
        # queries for retrievint all rows
        getVoucher = "SELECT * FROM `potonganharga` WHERE `idPotongan` = '" + kode + "';"

        #executing the quires
        self.cursor.execute(getVoucher)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            return False
        else:
            return True
    
    # Overloading (?)
    def insertTransaksi(self, *argv):
        if len(argv) == 1:
            self.tanpavoucher(argv[0])
        elif len(argv) == 2:
            self.pakevoucher(argv[0], argv[1])
    # kalau ga pake voucher
    def tanpavoucher(self, namaPelanggan):

        insertTransaksi = "INSERT INTO `transaksi` (`idTransaksi`, `namaPelanggan`, `status`, `idPotongan`, `Mulai`) VALUES (NULL, '" + namaPelanggan + "', 'belum selesai', NULL, '" + self.__addDataTransaksi['mulai'] + "')"

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
            if kodevoucher == 'null':
                # print(i[0],i[1])
                value = value + "(" + str(data[0][0]) + ", " + str(i[0]) + ", " + str(i[1]) + "),"
        insertDetail = insertDetail + value[:-1] + ";"
        
        # executing the quires
        self.cursor.execute(insertDetail)
        self.connection.commit()

        return True
    # kalau pake voucher
    def pakevoucher(self, namaPelanggan, kodevoucher):
        
        insertTransaksi = "INSERT INTO `transaksi` (`idTransaksi`, `namaPelanggan`, `status`, `idPotongan`, `Mulai`) VALUES (NULL, '" + namaPelanggan + "', 'belum selesai', " + kodevoucher + ", '" + self.__addDataTransaksi['mulai'] + "')"
        
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

    def viewPaket(self):
        
        getData     = "SELECT * FROM paket ORDER BY idPaket ASC;"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()
        # print(data)
        return list(data)

    def viewTransaksi(self):
        
        getData     = "SELECT * FROM transaksi ORDER BY idTransaksi DESC LIMIT 10;"

        self.cursor.execute(getData)
        data = self.cursor.fetchall()
        # print(data)
        return list(data)

    def detailTransaksi(self, idTransaksi):

        getDetail   = "SELECT * FROM detailpakaian WHERE `idTransaksi` = " + idTransaksi + ";"

        self.cursor.execute(getDetail)

        data = self.cursor.fetchall()

        return list(data)
    
    def findPaket(self, idPaket):

        getData     = "SELECT namaPaket FROM paket WHERE `idPaket` = " + str(idPaket) + "  LIMIT 1;"

        self.cursor.execute(getData)

        data = self.cursor.fetchall()
        
        return data[0][0]
    