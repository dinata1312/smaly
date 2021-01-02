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
            menu()
        else:
            self.__username    = rows[0][0]
            self.__namaLengkap = rows[0][2]

            #commiting the connection then closing it.
            self.connection.commit()
            self.connection.close()
            menu()
            # os.system('python adminPage.py')

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

def menu():
    os.system('cls')
    print("""
    ======================= S M A L Y =======================
    SELAMAT DATANG DI SISTEM MANAJEMEN LAUNDRY MILIK PAK EKO \n
    SILAHKAN INPUT NOMOR UNTUK MEMILIH PILIHAN\n
    1. Tambah transaksi baru
    2. Lihat Transaksi
    3. Menu Paket
    4. Pendapatan kotor 
    5. Keluar
    """)
    pilihan = int(input('Masukkan pilihan anda = '))

    if pilihan == 1 or pilihan == 2:
        os.system('python transaksi.py')
        transaksi = Transaksi()
        if pilihan == 1:
            transaksi.tambah()
        else:
            transaksi.lihat()
    elif pilihan == 3:
        os.system('python paket.py')
        paket     = Paket()
        paket.lihatMenu()
    elif pilihan == 4:
        os.system('python pendapatan.py')
        pendapatan= pendapatan()
        pendapatan.lihat()
    elif pilihan == 5:
        print('Terima kasih')
        print(login.username)
        input('Tekan ENTER untuk keluar')
        exit()
    else:
        print('Input yang dimasukkan salah! \ninput hanya boleh diisi angka 1, 2, 3, 4, dan 5 !')
        input('tekan ENTER untuk melanjutkan...')
        main()

def transaksi():
    os.system('cls')
    print("""
    ======================= S M A L Y =======================
    TAMBAH TRANSAKSI \n
    """)
    print("Tentukan jenis paket cuci : ")
    print("1. Pakaian harian\n2. Boneka\n")
    JenisCucian = input('Masukkan jenis cucian = ')


# ============================================
# INSERT COMMAND 
# # queries for inserting values
# insert1 = "INSERT INTO users(username, password, namaLengkap) VALUES('ninacutez', 'admin123', 'karenina cutes abis' );"

# #executing the quires
# cursor.execute(insert1)
# END INSERT COMMAND
# ============================================

login       = Login()
transaksi   = Transaksi()

if __name__ == '__main__':
    main()