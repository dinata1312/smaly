import pymysql
import os
from getpass import getpass
import controller as ct

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
    
    login = ct.Login(username, password)

    login.auth()

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
        
        if pilihan == 1:
            tambahTransaksi()
        else:
            lihatTransaksi()

    elif pilihan == 3:

        paket     = Paket()
        paket.lihatMenu()

    elif pilihan == 4:
        
        pendapatan= Pendapatan()
        pendapatan.lihat()

    elif pilihan == 5:
        print('Terima kasih')
        input('Tekan ENTER untuk keluar')
        exit()
    else:
        print('Input yang dimasukkan salah! \ninput hanya boleh diisi angka 1, 2, 3, 4, dan 5 !')
        input('tekan ENTER untuk melanjutkan...')
        main()

def tambahTransaksi():

    transaksi = ct.Transaksi()

    os.system('cls')
    loop = True
    count = 0
    loopDetail = True
    while loop == True:
        if loopDetail == True:
            print("""
            ======================= S M A L Y =======================
            TAMBAH TRANSAKSI \n
            """)
            print("Tentukan jenis paket cuci : ")

            banyakPaket     = list(transaksi.viewPaket() )

            idPaket     = []
            hitung       = 1

            for i in banyakPaket:
                print(hitung, end=". ")
                print(i[1])
                # print("1." . banyakPaket[i][1])
                idPaket.append(i[0])
                hitung+=1
            print("99. Selanjutnya")

            JenisCucian = int(input('Masukkan jenis cucian = ') )
            
            if JenisCucian not in idPaket and JenisCucian != 99:

                print("Input salah ! masukkan input dengan benar !")
                input("\nTekan ENTER untuk melanjutkan")
                os.system('cls')
                continue

            elif JenisCucian in idPaket:

                berat       = int(input('Masukkan berat = '))
                transaksi.addDetail(JenisCucian, berat, count)
                count = count + 1

            else:
                loopDetail = False
                namaPelanggan = input("Masukkan nama pelanggan = ")
                continue

        else:
            ansVoucher = int(input("apakah punya kode voucher?\n1. Ya\n2. Tidak \nJawaban anda = "))

            if ansVoucher > 2 and ansVoucher < 1:

                print("Input yang dimasukkan salah !")
                input("tekan ENTER untuk melanjutkan")

            elif ansVoucher == 1:

                kodevoucher = input("Masukkan kode voucher!")

                if transaksi.verifyVoucher(kodevoucher) == False :
                    print("kode voucher gagal digunakan !")
                else:
                    print("kode voucher berhasil digunakan")
                    input("Tekan ENTER untuk melanjutkan")
                    transaksi.insertTransaksi(namaPelanggan, kodevoucher)
                    loopDetail = False
                    loop       = False

            elif ansVoucher == 2:
                    transaksi.insertTransaksi(namaPelanggan)
                    loopDetail = False
                    loop       = False
    print()
    print("==========Transaksi selesai==========")
    print("\ntekan ENTER untuk melanjutkan")

if __name__ == '__main__':
    main()