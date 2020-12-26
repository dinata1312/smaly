import pymysql
import os
from getpass import getpass

class Login:
    def __init__(self):
        #database connection
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="smaly" )
        self.cursor = self.connection.cursor()

        self.__username = ''
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

    def auth(self, username, password):

        # queries for retrievint all rows
        getUser = "SELECT * FROM `users` WHERE `username` = '" + username + "' AND `password` = '" + password + "';"

        #executing the quires
        self.cursor.execute(getUser)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print('username atau password salah !')
            input('\ntekan ENTER untuk lanjut')
            main()
        else:
            self.__username    = rows[0][0]
            self.__namaLengkap = rows[0][2]

            #commiting the connection then closing it.
            self.connection.commit()
            self.connection.close()
        
            os.system('python adminPage.py')




def main():
    os.system('cls')
    print("""
======================= S M A L Y =======================
SELAMAT DATANG DI SISTEM MANAJEMEN LAUNDRY MILIK PAK EKO \n
SILAHKAN LOGIN TERLEBIH DAHULU\n
    """)
    username = input('Masukkan username = ')
    # password = input('Masukkan password = ')
    password = getpass(prompt = 'Masukkan password = ', stream=None)
    
    login.auth(username, password)


# ============================================
# INSERT COMMAND 
# # queries for inserting values
# insert1 = "INSERT INTO users(username, password, namaLengkap) VALUES('ninacutez', 'admin123', 'karenina cutes abis' );"

# #executing the quires
# cursor.execute(insert1)
# END INSERT COMMAND
# ============================================

login = Login()

if __name__ == '__main__':
    main()