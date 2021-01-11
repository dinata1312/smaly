import pymysql
import os

from getpass import getpass

import login as LoginController
import transaksi as TransaksiController
import paket as PaketController
import cekstatus as CekStatusController
import pendapatan as PendapatanController

class Main:

    def main(self):

        os.system('cls')
        print("======================= S M A L Y =======================")
        print("SELAMAT DATANG DI SISTEM MANAJEMEN LAUNDRY MILIK PAK EKO \n")
        print("Siapakah anda? \n")
        print("1. Pelanggan")
        print("2. Pegawai")
        print("99. keluar\n")

        answer = int(input("Isikan jawaban anda = "))
        if answer == 1 : 
            self.cekstatus()
        elif answer == 2 :
            self.login()
        elif answer == 99 :
            exit()
        else:
            print('Input yang dimasukkan salah! \ninput hanya boleh diisi angka 1 dan 2!')
            input('tekan ENTER untuk melanjutkan...')
            self.main()
          
    def login(self):
        
        os.system('cls')
        print("SILAHKAN LOGIN TERLEBIH DAHULU\n")
        
        username = input('Masukkan username = ')
        # password = input('Masukkan password = ')
        password = getpass(prompt = 'Masukkan password = ', stream="*")
        
        login = LoginController.Login(username, password)

        login.auth()
   
    def cekstatus(self):

        os.system('cls')
        transaksi = TransaksiController.Transaksi()
        print()
        print("Masukkan id pesanan untuk melihat status pakaian, untuk kembali ke menu ketik 0")
        print()
        cekStatus = CekStatusController.CekStatus()
        answer = input("Jawaban = ")

        if answer == 0:
            self.main()

        else :
            status = cekStatus.viewStatus(answer)
            
            if len(status) > 0:
                for i in status:
                    print("||==============================================||")
                    print("|| ID Transaksi\t\t= " + str(i[0]) + "\t\t\t||")
                    print("|| Nama Pelanggan\t= " + str(i[1]) + "\t\t||")
                    print("|| Status\t\t= " + str(i[2]) + "\t\t||")
                    print("|| Tanggal Pemesanan\t= " + str(i[3]) + "\t\t||" )
                    print("||----------------------------------------------||")

                    
                    idTransaksi = answer
                    detailnya = list(transaksi.detailTransaksi(idTransaksi))
                    total = 0

                    print("||==============================================||")
                    print("|| Paket\t|| Berat\t || Harga \t||")
                    print("||==============================================||")

                    for j in detailnya:
                        
                        namaPaket = transaksi.findPaket(j[2])

                        print("|| " + str(namaPaket[0][1]) + "\t|| " + str(j[3]) + " kg\t\t || " + str(namaPaket[0][2]) + "\t||")

                        print("||----------------------------------------------||")
                        total = total + namaPaket[0][2]
                    
                    print("||TOTAL HARGA \t\t\t   Rp" + str(total) + "\t||")
                    print("||==============================================||")

                    print()
                    
            else:
                print("mohon maaf ID Pesanan tidak ditemukan !")

            input("tekan ENTER untuk keluar")
            self.main()

class Menu():
    def menu(self):
        
        os.system('cls')
        print("======================= S M A L Y =======================")
        print("SELAMAT DATANG DI SISTEM MANAJEMEN LAUNDRY MILIK PAK EKO \n")
        print("SILAHKAN INPUT NOMOR UNTUK MEMILIH PILIHAN\n")
        print("1. Tambah transaksi baru")
        print("2. Lihat Transaksi")
        print("3. Menu Paket")
        print("4. Pendapatan kotor ")
        print("5. Keluar")

        pilihan = int(input('Masukkan pilihan anda = '))

        if pilihan == 1 or pilihan == 2:
            
            if pilihan == 1:
                self.tambahTransaksi()
            else:
                self.lihatTransaksi()

        elif pilihan == 3:
            self.menupaket()

        elif pilihan == 4:
            self.pendapatan()

        elif pilihan == 5:
            print('Terima kasih')
            input('Tekan ENTER untuk keluar')
            Main().main()
        else:
            print('Input yang dimasukkan salah! \ninput hanya boleh diisi angka 1, 2, 3, 4, dan 5 !')
            input('tekan ENTER untuk melanjutkan...')
            Menu.menu()

    def tambahTransaksi(self):

        os.system('cls')

        paket     = PaketController.Paket()
        transaksi = TransaksiController.Transaksi()

        loop = True
        count = 0
        loopDetail = True
        while loop == True:
            if loopDetail == True:

                print()
                print("======================= S M A L Y =======================")
                print("TAMBAH TRANSAKSI")
                print()
                paket = PaketController.Paket()

                dataPaket = list(paket.viewPaket() )

                print("||=======================================================||")
                print("||ID ||\tNama Paket\t|| Durasi\t|| Harga\t ||")
                print("||=======================================================||")

                for i in dataPaket:
                    print("||" + str(i[0]) + "  || " + str(i[1]) + "\t|| " + str(i[4]) + " hari\t|| Rp" + str(i[2]) + "\t ||")

                print("||=======================================================||")

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
                print("--------------------------")
                print("99. Selanjutnya")
                print("0. Kembali")

                JenisCucian = int(input('Masukkan jenis cucian = ') )
                
                if JenisCucian not in idPaket and JenisCucian !=0 and JenisCucian !=99:

                    print("Input salah ! masukkan input dengan benar !")
                    input("\nTekan ENTER untuk melanjutkan")
                    os.system('cls')
                    continue

                elif JenisCucian in idPaket:

                    berat       = int(input('Masukkan berat = '))
                    transaksi.addDetail(JenisCucian, berat, count)
                    count = count + 1

                elif JenisCucian == 0:
                    self.menu()

                else:

                    namaPelanggan = input("Masukkan nama pelanggan = ")
                    
                    transaksi.insert(namaPelanggan)
                    loopDetail = False
                    loop       = False

        print()
        print("==========Transaksi selesai==========")
        input("\ntekan ENTER untuk lihat transaksi")
        self.lihatTransaksi()

    def lihatTransaksi(self):

        os.system('cls')

        transaksi = TransaksiController.Transaksi()

        dataTransaksi = list(transaksi.viewTransaksi() )

        print("||======================================================================================||")
        print("|| ID\t|| Nama Pelanggan\t || Status\t  || Tanggal Pesan \t|| Total \t||")
        print("||======================================================================================||")

        if len(dataTransaksi) < 1:

            print("||------------------------------------ Data kosong -------------------------------------||")
        else:

            for i in dataTransaksi:

                dataDetail = transaksi.detailTransaksi(i[0])
                total = 0

                for j in dataDetail:
                    
                    harga = transaksi.findPaket(j[2])
                    
                    total = total + harga[0][2]

                if i[2] == 'selesai':
                    print("|| " + str(i[0]) + "\t|| " + str(i[1]) + "\t\t || " + str(i[2]) + "\t  || " + str(i[3]) + "\t\t|| Rp" + str(total) + "\t||")
                else:
                    print("|| " + str(i[0]) + "\t|| " + str(i[1]) + "\t\t || " + str(i[2]) + " || " + str(i[3]) + "\t\t|| Rp"  + str(total) + "\t||")
            
        print("||======================================================================================||")
        print()
        print("Masukkan id untuk melihat pesanan, untuk kembali ke menu ketik 0")
        answer = int(input("Jawaban = ") )

        if answer == 0:

            self.menu()

        else:

            os.system('cls')

            idTransaksi = answer
            detailnya = list(transaksi.detailTransaksi(idTransaksi))

            print("||=====================================||")
            print("|| Paket\t|| Berat\t || Harga \t||")
            print("||=====================================||")

            for i in detailnya:
                
                namaPaket = transaksi.findPaket(i[2])
                print("|| " + str(namaPaket[0][1]) + "\t|| " + str(i[3]) + " kg\t\t || " + str(namaPaket[0][2]) + "\t||")
                print("||----------------------------------------------||")
                
            print()
            print("Opsi: ")
            print("1. Selesai\n2. Kembali ke menu")
            print()
            answer = int(input("Jawaban anda = ") )
            if answer == 1:
                transaksi.update(idTransaksi) 
                print("Data berhasil diperbarui !")
                input("Tekan ENTER untuk kembali ke lihat transaksi")
            else:
                input("Tekan ENTER untuk kembali ke lihat transaksi")
            Menu().lihatTransaksi()

    def menupaket(self):
        
        os.system('cls')

        paket = PaketController.Paket()
        dataPaket = list(paket.viewPaket() )

        print("||=======================================================||")
        print("||ID ||\tNama Paket\t|| Durasi\t|| Harga\t ||")
        print("||=======================================================||")

        for i in dataPaket:
            print("||" + str(i[0]) +  " || \t" + str(i[1]) + "\t|| " + str(i[4]) + " hari\t|| Rp" + str(i[2]) + "\t ||")

        print("||=======================================================||")

        print()
        print("Kamu mau apa?")
        print("1. Tambah paket")
        print("2. Hapus paket")
        print("3. Kembali")
        answer = input("Jawaban = ")

        if answer == "1":
            self.tambahpaket()
        elif answer == "2":
            self.hapuspaket()
        elif answer == "3":
            self.menu()
        else:
            print('Input yang dimasukkan salah! \ninput hanya boleh diisi angka 1 dan 2!')
            input('tekan ENTER untuk melanjutkan...')
            PaketController.menupaket()

    def tambahpaket(self):

        paket = PaketController.Paket()

        os.system('cls')
        print("""
        ======================= S M A L Y =======================
        TAMBAH PAKET \n
        """)
        print("Buat Data Baru : ")

        namaPaket = input('Masukkan nama Paket = ') 
        harga = int(input('Masukkan harga = '))
        jenis = input('Masukkan jenis = ')
        durasi = int(input('Masukkan durasi pengerjaan = '))
        
        print()
        
        # VALIDASI INPUT
        if paket.insert(namaPaket, harga, jenis, durasi) == False:
            print("==========Paket GAGAL ditambahkan==========")
            print("Mohon periksa data yang diinputkan!")
            print("**Nama paket yang didaftarkan tidak boleh sama dengan nama yang sudah pernah diinputkan !")
            input("\ntekan ENTER untuk kembali ke menu paket")
            self.menupaket()
        else:
            print("==========Paket berhasil ditambahkan==========")
            input("\ntekan ENTER untuk melihat paket")
            self.menupaket()

    def hapuspaket(self):

        os.system('cls')

        paket = PaketController.Paket()
        dataPaket = list(paket.viewPaket() )

        print("||=======================================================||")
        print("||ID ||\tNama Paket\t|| Durasi\t|| Harga\t ||")
        print("||=======================================================||")

        for i in dataPaket:
            print("||" + str(i[0]) + "  || " + str(i[1]) + "\t|| " + str(i[4]) + " hari\t|| Rp" + str(i[2]) + "\t ||")

        print("||=======================================================||")

        print()
        idPaket = input("Masukkan id data paket yang ingin anda hapus = ")
        paket.delete(idPaket)

        print()
        print("=====Paket berhasil dihapus=====")
        print("\ntekan ENTER untuk melihat paket")
        self.menupaket()

    def pendapatan(self):
        
        pendapatan = PendapatanController.Pendapatan()
        transaksi  = TransaksiController.Transaksi()

        bulan      = int(input("Masukkan bulan (1-12) = ") )
        tahun      = int(input("Masukkan tahun = ") )

        if int(bulan) > 0 and int(bulan) < 13 and int(tahun) > 2000:

            dataPendapatan  = pendapatan.byBulan(bulan, tahun)
            totalTransaksi  = 0
            totalPendapatan = 0

            # JIKA ADA DATA TRANSAKSI 
            if len(dataPendapatan) > 0:

                for i in dataPendapatan:
                    
                    totalTransaksi = totalTransaksi + 1

                    
                    detailTransaksi = transaksi.detailTransaksi(i[0])

                    for j in detailTransaksi:
                        
                        harga = transaksi.findPaket(j[2])
                        totalPendapatan = totalPendapatan + harga[0][2]
            
            # JIKA TIDAK ADA TRANSAKSI
            else:

                totalTransaksi = "belum ada"
                totalPendapatan = 0

            print("||==============================================||")
            print("|| Tahun\t\t= " + str(tahun) + "\t\t\t||")
            print("|| Bulan\t\t= " + str(bulan) + "\t\t\t||")

            if totalPendapatan == "belum ada":
                print("|| Jumlah Transaksi\t= " + str(totalTransaksi) + "\t\t||")
            else:
                print("|| Jumlah Transaksi\t= " + str(totalTransaksi) + "\t\t\t||")
            if totalPendapatan > 999:
                print("|| Total pendapatan\t= Rp" + str(totalPendapatan) + "\t\t||" )
            else:
                print("|| Total pendapatan\t= Rp" + str(totalPendapatan) + "\t\t\t||" )
            print("||----------------------------------------------||")
            
        else:
            print("Input yang dimasukkan salah !")
            print("Input harus angka mulai dari 1 - 12 untuk menunjukkan bulan !")

        input("tekan ENTER untuk kembali")
        self.menu()

if __name__ == '__main__':
    Main().main()
