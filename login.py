import pymysql
import os

from main import Menu

from getpass import getpass
from datetime import datetime

class Login():
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
            Menu().menu()
            # os.system('python adminPage.py')
