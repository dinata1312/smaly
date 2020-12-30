import login
import os

class Users:
    def __init__(self):
        self.__username    = ''
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

def main():
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
        pendapatan= Pendapatan()
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

user = Login()
if __name__ == '__main__':
    main()