import mysql.connector 
import pwinput
import math
from prettytable import PrettyTable
import time, datetime
import sys
import re
from termcolor import colored
import os
os.system("cls")


# mendefinisikan sebuah Pasien, Method __init__ ini akan menginisialisasi semua atribut dari objek Pasien.
class Pasien:
    def __init__(self,id_pasien, nama_pasien, umur_pasien, alamat, diagnosa):
        self.id_pasien = id_pasien
        self.nama_pasien = nama_pasien
        self.umur_pasien = umur_pasien
        self.alamat = alamat
        self.diagnosa = diagnosa
        self.next = None

# Constructor untuk kelas LinkedList.
class LinkedList:
    def __init__(self):
        # Menginisialisasi atribut head dan saldo.
        self.head = None
        self.saldo = 1000000000

    # Menambahkan objek Pasien baru ke akhir linked list.
    def tambah_pasien(self, id_pasien, nama_pasien, umur_pasien, alamat, diagnosa):
        new_pasien = Pasien(id_pasien, nama_pasien, umur_pasien, alamat, diagnosa)

        if not self.head:
            self.head = new_pasien
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_pasien

    # Menampilkan data pasien yang terdaftar dalam bentuk tabel.
    def tampilan_pasien(self):
        if not self.head:
            print(">>> Tidak Ada Data Pasien Yang Terdaftar. <<<")
        else:
            v = 1
            current = self.head
            table = PrettyTable(["NO", "ID", "NAMA", "UMUR", "ALAMAT", "DIANOGSA"])
            while current:
                table.add_row([v, current.id_pasien, current.nama_pasien, current.umur_pasien, current.alamat, current.diagnosa])
                v += 1
                current = current.next
            print (table)

    # Mengupdate data pasien yang sudah terdaftar.
    def update_pasien(self, index, id_pasien, nama_pasien, umur_pasien, alamat, diagnosa):
        if index:
            index.id_pasien = id_pasien
            index.nama_pasien = nama_pasien
            index.umur_pasien = umur_pasien
            index.alamat = alamat
            index.diagnosa = diagnosa
            print()
            print(">>> Data Pasien Berhasil di Update. <<<")
            print()
        else:
            print(">>> Data Pasien Tidak Ditemukan. <<<")

    # menghapus data pasien pada linked list berdasarkan index
    def hapus_pasien(self, index):
        if not self.head:
            print(">>> Tidak Ada Nama Pasien yang Terdaftar. <<<")
            return
        
        if index == 1:
            self.head = self.head.next
            print()
            print(">>> Data Pasien Berhasil Dihapus. <<<")
            print()
            return
        
        prev = None
        current = self.head
        s = 1
        while current and s != index:
            prev = current
            current = current.next
            s += 1

        if not current:
            print(">>> Pasien dengan Index tersebut Tidak Ditemukan. <<<")
            return
        
        prev.next = current.next
        current.next = None
        print()
        print(">>> Data Pasien Berhasil di Hapus. <<<")
        print()

    # mengurutkan elemen berdasarkan nilai ID pasien secara ascending.
    def shell_sort(self):
        n = self.get_length()
        gap = n // 2
        while gap > 0:
            for w in range(gap, n):
                temp_node = self.get_node_at_index(w)
                temp_id_pasien = temp_node.id_pasien
                temp_nama_pasien = temp_node.nama_pasien
                temp_umur_pasien = temp_node.umur_pasien
                temp_alamat = temp_node.alamat
                temp_diagnosa = temp_node.diagnosa
                y = w
                while y >= gap and self.get_node_at_index(y - gap).id_pasien > temp_id_pasien:
                    node_y_gap = self.get_node_at_index(y - gap)
                    self.get_node_at_index(y).id_pasien = node_y_gap.id_pasien
                    self.get_node_at_index(y).nama_pasien = node_y_gap.nama_pasien
                    self.get_node_at_index(y).umur_pasien = node_y_gap.umur_pasien
                    self.get_node_at_index(y).alamat = node_y_gap.alamat
                    self.get_node_at_index(y).diagnosa = node_y_gap.diagnosa
                    y -= gap
                self.get_node_at_index(y).id_pasien = temp_id_pasien
                self.get_node_at_index(y).nama_pasien = temp_nama_pasien
                self.get_node_at_index(y).umur_pasien = temp_umur_pasien
                self.get_node_at_index(y).alamat = temp_alamat
                self.get_node_at_index(y).diagnosa = temp_diagnosa
            gap //= 2

    # Buat return fungsi cari_pasien
    def cari1(self,index):
        return self.cari_pasien(index)
    
    # mengkonversi data dari Linked List ke dalam bentuk array.
    def to_array(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.id_pasien)
            current_node = current_node.next
        return array
    
    # mendapatkan node pada index tertentu di dalam Linked List.
    def getindex(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1

    # mendapatkan node dengan id_pasien tertentu di dalam Linked List.
    def get_id(self, id_pasien):
        current_node = self.head
        current_id_pasien = id_pasien

        while current_node is not None:
            if current_id_pasien == id_pasien:
                return current_node
            
            current_node = current_node.next
            current_id_pasien = id_pasien

    # mendapatkan jumlah node yang ada di dalam Linked List.
    def get_length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # mendapatkan node pada index tertentu di dalam Linked List.
    def get_node_at_index(self, index):
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node
            count += 1
            current_node = current_node.next
        return None

    # mencari pasien dengan id_pasien tertentu di dalam Linked List. (jump search)
    def cari_pasien(self):
        carii = input("Masukkan ID pasien yang ingin di cari: ").replace (" ","")
        print()
        if not carii.isdigit():
            print(">>> ID Pasien Harus Berupa Angka. <<<")
            print()
            return
        
        daftar_pasien = self.head
        found = False
        while daftar_pasien is not None:
            # Konversi data Linked List ke array
            arr = self.to_array()
            n = len(arr)
            jump = int(math.sqrt(n))
            left, right = 0, 0
            # Melakukan jump search pada array
            while right < n and int(arr[right]) < int(carii):
                left = right
                right = min(n - 1, right + jump)
            for i in range(left, right + 1):
                if arr[i] == carii:
                    node = self.getindex(i)
                    print(f"Data Pasien Ditemukan pada index ke-{i+0}")
                    print(f"ID Pasien: {node.id_pasien}")
                    print(f"Nama Pasien: {node.nama_pasien}")
                    print(f"Umur Pasien: {node.umur_pasien}")
                    print(f"Alamat Pasien: {node.alamat}")
                    print(f"Diagnosa Pasien: {node.diagnosa}")
                    print()
                    found = True
                    return

            daftar_pasien = daftar_pasien.next
        if not found:
            print(">>> ID Pasien yang Anda Masukkan Salah atau Tidak Ada. <<<")
            print()
            return
        
    # mencari pasien dengan id_pasien tertentu di dalam Linked List
    def cari_pasien_regisAdmin(self, id_pasien):
        current = self.head
        while current is not None:
            if current.id_pasien == id_pasien:
                return current
            current = current.next
        return None

    # memesan kamar pasien di rumah sakit
    def pesan_kamar(self):
        table = PrettyTable()
        table.field_names = ["No.", "Jenis Kamar", "Deskripsi", "Harga per hari"]
        table.add_row(["1", "Intensive Care Unit (ICU)", "Pasien Harus Cepat mendapatkan perawatan, ruangan dilengkapi peralatan canggih", "Rp. 350.000"])
        table.add_row(["2", "High Care Unit (HCU)", "Untuk pasien rawat inap, ruangan dilengkapi peralatan canggih", "Rp. 400.000"])
        table.add_row(["3", "Intensive Coronary Care Unit (ICCU)", "Ruangan untuk penderita penyakit jantung, kedap suara dan hening", "Rp. 450.000"])
        table.add_row(["4", "Neonatal Intensive Care Unit (NICU)", "Ruangan untuk yang melahirkan, dilengkapi ruang tunggu orang tua", "Rp. 500.000"])
        table.add_row(["5", "Pediatric Intensive Care Unit (PICU)", "Ruangan untuk bayi dan 18 tahun, dilengkapi ruang tunggu orang tua", "Rp. 500.000"])
        print("----PILIH KAMAR PASIEN----")
        print(table)

        id_pasien = input("Masukkan ID Pasien yang Telah Terdaftar: ")
        print()
        daftar_pasien = self.head
        found = False
        while daftar_pasien is not None:
            if daftar_pasien.id_pasien == id_pasien:
                aa = int(input("Pilih Nomor Jenis Kamar yang Anda Inginkan :"))
                if aa < 1 or aa > 5:
                    print(">>> Nomor Kamar Tidak Valid. <<<")
                    return
                days = int(input("Masukkan Jumlah Hari Menginap: "))
                os.system('cls')
                if days < 1:
                    print(">>> Jumlah Hari Tidak Valid. <<<")
                    return
                prices = [350000, 400000, 450000, 500000, 500000]
                total = prices[aa - 1] * days
                if self.saldo < total:
                    print(">>> Saldo Anda Tidak Mencukupi untuk Memesan Kamar Ini. <<<")
                    return
                self.saldo -= total
                rows = str(table).split("\n")[3:-1]
                cells = [row.split("|")[1:-1] for row in rows]
                kamar = cells[aa - 1][1]

                invoice = f"{'RUMAH SAKIT BERJAYA':^95}\n\n"
                invoice += f"{'INVOICE':^95}\n\n"
                invoice += f"{'Nama Kamar':<30} {'Harga/Hari':<20} {'Jumlah Hari':<20} {'Total Harga':<20}\n"
                invoice += "-" * 100 + "\n"
                invoice += f"{kamar:<1} Rp.{prices[aa-1]:<20,} {days:<20,} Rp.{total:<20,}\n"
                invoice += "-" * 100 + "\n"
                invoice += f"{'Total Pembayaran':<60} Rp.{total:<15,}\n\n"
                invoice += ">>> Terima Kasih Telah Memesan Kamar di Rumah Sakit Berjaya. <<<\n"
        
                # menulis invoice ke dalam file txt
                with open("invoice_kamar.txt", "w") as file:
                    file.write(invoice)

                print("\n")
                print(invoice)

                print()
                print(f"Berhasil Memesan Kamar,{kamar}dengan Biaya Rp.{total:,}")
                print()
                print("============================================================")
                print(         f"Saldo Anda sekarang adalah Rp.{ana.saldo:,}       ")
                print("============================================================")
                print()
                return ana.saldo
                         
            daftar_pasien = daftar_pasien.next
        if not found:
            print(">>> ID Pasien yang Anda Masukkan Salah atau Tidak Ada. <<<")
            print()
            return
        
ana = LinkedList()

apotek = {'paracetamol': {'stok': 100,'harga': 5000}, 
            'amoxicillin': {'stok':100,'harga': 10000}, 
            'vitamin C': {'stok':100,'harga': 2000},
            'ambroxol': {'stok':100,'harga': 25000},
            'captopril': {'stok':100,'harga': 30000}}

# menambah stok ketersediaan obat
def tambah_obat(apotek, nama_obat, harga, stok):
    if nama_obat in apotek:
        print(f"Obat {nama_obat} Sudah Tersedia.")
    else:
        apotek[nama_obat] = {'Harga': harga, 'Stok': stok}
        print(f"Obat {nama_obat} Berhasil Ditambahkan dengan Harga {harga} dan Stok {stok}.")

# menampilkan tampilan obat yang tersedia
def tampilan_obat(apotek):
    table = PrettyTable()
    table.field_names = ["Obat", "Harga", "Stok"]
    for obat, data in apotek.items():
        table.add_row([obat, data['harga'], data['stok']])
    # Menambahkan warna pada header tabel
    print()
    table_title = colored("Selamat Datang di Apotek Berjaya, Berikut Adalah Obat Yang Tersedia^_^", "green", attrs=["bold"])
    print(table_title)
    print(table)
    print()

# membeli obzt yang tersedia di apotek
def beli_obat(apotek):
    while True:
        try:
            nama_obat = input("Masukkan Nama Obat yang Ingin Dibeli: ").strip().replace("\t","")
            jumlah = int(input("Masukkan Jumlah Obat yang Ingin Dibeli: "))
            break
        except ValueError:
            print()
            print(">>> Input Tidak Valid. Silahkan Masukkan Angka untuk Jumlah Obat. <<<")
            print()
            menu_pasien()
            break

    if nama_obat in apotek:
        if apotek[nama_obat]['stok'] >= jumlah:
            total_harga = apotek[nama_obat]['harga'] * jumlah
            if total_harga > ana.saldo:
                print(">>> Maaf, Saldo Anda Tidak Cukup. <<<")
                return False
            apotek[nama_obat]['stok'] -= jumlah
            ana.saldo -= total_harga
            print(f"Anda Telah Membeli {jumlah} {nama_obat} dengan Total Harga {total_harga}.")
            print(f"Sisa Saldo Anda: {ana.saldo}")
            # Tambahkan fitur invoice
            with open('invoice.txt', 'a') as f:
                f.write ("=====================================\n")
                f.write ("|    S T R U K  P E M B E L I A N   |\n")
                f.write ("=====================================\n")
                f.write(f"Nama Obat: {nama_obat}\n")
                f.write(f"Jumlah: {jumlah}\n")
                f.write(f"Total Harga: {total_harga}\n")
                f.write(f"Sisa Saldo: {ana.saldo}\n")
                f.write ("\n=====================================")
            return True
        else:
            print(f"Maaf, Stok Obat {nama_obat} Tidak Cukup.")
            return False
    else:
        print(f"Maaf, Obat {nama_obat} Tidak Tersedia.")
        return False

# informasi kamar rumah sakit
def informasi_kamar():
    print("    ---------------------------  ROOMS INFO Hospital  -----------------------------    ")
    print("")
    print("== Intensive Care Unit (ICU) ==")
    print("---------------------------------------------------------------------------------------")
    print("ICU adalah ruangan khusus bagi pasien kritis yang perlu perawatan intensif dan ")
    print("pengawasan terus menerus")

    print("== High Care Unit (HCU) ==")
    print("---------------------------------------------------------------------------------------")
    print("HCU adalah pelayanan yang dikendalikan ke rauan rawat inap")
    print("ruangan ini di peruntukkan kepada pasien yang sudah kondisi membaik")
    print("namun masih perlu pengawasan ketat oleh tenaga medis\n")

    print("== Intensive Coronary Care Unit (ICCU) ==")
    print("---------------------------------------------------------------------------------------")
    print("Ruangan ini cocok untuk penderita penyakit jantung.\n")
    
    print("== Neonatal Intensive Care Unit (NICU) ==")
    print("---------------------------------------------------------------------------------------")
    print("Ruangan ini cocok untuk pelayanan bersalin/melahirkan,")

    print("== Pediatric Intensive Care Unit (PICU) ==")
    print("---------------------------------------------------------------------------------------")
    print("Ruangan ini diperuntukkan bagi bayi yang tidak diambil NICU serta anak hingga 18 tahun.")
    print()
    while True:
        try:
            n=int(input("0-KEMBALI\n -> "))
            if n==0:
                os.system('cls')
                return
            else:
                raise ValueError
        except ValueError:
            print
            print(">>> Inputan Tidak Valid. Masukkan Angka 0 untuk Kembali. <<<") 
            print()

# tampilan menu pasien
def menu_pasien():
    while True:
        print("|===================================|")
        print('|            MENU PASIEN            |')
        print("|===================================|")
        print("||  1  | Informasi Kamar           ||")
        print("||  2  | Pemesanan                 ||")
        print("||  3  | Apotek                    ||")
        print("||  4  | Liat Saldo                ||")
        print("||  5  | Tambah Saldo              ||")
        print("||  6  | Keluar Menu Pasien        ||")
        print("||  7  | Exit                      ||")
        print("|===================================|")
        print()
        
        ch = (input("Pilih Menu yang Diinginkan: ")).replace (" ","")

        if ch == "1":
            os.system('cls')
            informasi_kamar()

        elif ch == "2":
            os.system('cls')
            ana.pesan_kamar()

        elif ch == "3":
            os.system('cls')
            tampilan_obat(apotek)
            beli_obat(apotek)

        elif ch == "4":
            os.system('cls')
            print("=======================")
            print("Saldo Anda:",ana.saldo)
            print("=======================")
            print()

        elif ch == "5":
            os.system('cls')
            print()
            inputsaldo = int(input("Tambah Saldo: "))
            ana.saldo += inputsaldo
            print()

        elif ch == "6":
            os.system('cls')
            login()
            break

        elif ch == "7":
            os.system('cls')
            sys.exit(">>> PROGRAM TELAH SELESAI, TERIMAKASIH SAMPAI JUMPA LAGI😊 <<<")
    
        else:
            print()
            print(">>> Pilihan Tidak Valid. Silakan Coba Lagi. <<<")
            print()

# tampilan menu admin
def menu_admin():
    while True:
        print("|====================================================|")
        print('|                      MENU ADMIN                    |')
        print("|====================================================|")
        print("||  1  | Registrasi Pasien                          ||")
        print("||  2  | Read Data Pemeriksaan Pasien               ||")
        print("||  3  | Update Data Pasien                         ||")
        print("||  4  | Delete Data Pasien                         ||")
        print("||  5  | Sorting Data pasien                        ||")
        print("||  6  | Searching Data Pasien                      ||")
        print("||  7  | Keluar Menu Admin                          ||")
        print("||  8  | Exit                                       ||")
        print("|====================================================|")
        print()
        tanya = input("Inputkan Pilihan Anda : ")

        if tanya == "1":
            os.system('cls')
            while True:
                id_pasien = input("Masukkan Id Pasien (maksimal 3 angka): ")
                print()
                # memeriksa apakah ID pasien sudah terdaftar atau belum
                if ana.cari_pasien_regisAdmin(id_pasien) is not None:
                    print(f">>> ID pasien {id_pasien} sudah terdaftar. <<<")
                    print()
                    menu_admin()
                elif len(id_pasien) > 3:
                    print(">>> ID Pasien Tidak Boleh Lebih dari 3 Angka. <<<")
                    print()
                    menu_admin()
                elif not re.match("^[0-9]{3}$", id_pasien):
                    print(">>> ID Pasien Harus Berupa 3 Angka. <<<")
                    print()
                    menu_admin()
                elif re.search("[\s,.!]", id_pasien):
                    print(">>> ID Pasien Tidak Boleh Mengandung Spasi, Titik, Koma, atau Tanda Seru. <<<")
                    print()
                    menu_admin()
                else:
                    break
            
            while True:
                nama_pasien = input("Masukkan Nama Pasien: ")
                if not re.match("^[a-zA-Z ]+$", nama_pasien):
                    print()
                    print(">>> Nama Pasien Harus Berupa Huruf. <<<")
                    print()
                    menu_admin()
                else:
                    break
            
            while True:
                umur_pasien = input("Masukkan Umur Pasien: ")
                if not re.match("^[0-9]+$", umur_pasien):
                    print()
                    print(">>> Umur Pasien Harus Berupa Angka. <<<")
                    print()
                    menu_admin()
                else:
                    break
            
            while True:
                alamat = input("Masukkan Alamat Pasien: ")
                if not re.match("^[a-zA-Z0-9 ]+$", alamat):
                    print()
                    print(">>> Alamat Pasien Harus Berupa Huruf dan Angka. <<<")
                    print()
                    menu_admin()
                else:
                    break
            
            while True:
                diagnosa = input("Masukkan Penyakit yang di Diagnosa: ")
                if not re.match("^[a-zA-Z ]+$", diagnosa):
                    print()
                    print(">>> Penyakit Harus Berupa Huruf. <<<")
                    print()
                    menu_admin()
                else:
                    break

            ana.tambah_pasien(id_pasien, nama_pasien, umur_pasien, alamat, diagnosa)
            print()
            print(">>> Data Pasien Berhasil di Tambahkan. <<<")
            print()


        elif tanya == "2":
            os.system('cls')
            ana.tampilan_pasien()
            print()

        elif tanya == "3":
            os.system('cls')
            ana.tampilan_pasien()
            index = int(input("Masukkan Nomor Pasien yang Ingin Anda Update: "))
            print()
            if index > 0 and index <= ana.get_length():
                jj = ana.getindex(index -1)
                if jj:
                    id_Pasienbaru = input("Masukkan ID Pasien Terbaru: ")
                    nama_pasienbaru = input("Masukkan Nama Pasien Terbaru: ")
                    umur_pasienbaru = input("Masukkan Umur Pasien Terbaru: ")
                    alamat_baru = input("Masukkan Alamat Pasien Terbaru: ")
                    diagnosa_baru = input("Masukkan Penyakit yang sedang di Diagnosa: ")
                    ana.update_pasien(jj, id_Pasienbaru, nama_pasienbaru, umur_pasienbaru, alamat_baru, diagnosa_baru)
                else:
                    print(">>> Pasien yang Anda Cari Tidak Ditemukan. <<<")

        elif tanya == "4":
            os.system('cls')
            ana.tampilan_pasien()
            while True:
                index_input = input("Masukan Nomor Pasien Jika ingin Menghapus Data Pasien: ")
                if index_input.isdigit():
                    index = int(index_input)
                    np = ana.getindex(index - 1)
                    if np:
                        ana.hapus_pasien(index)
                        break
                    else:
                        print()
                        print(f"Data Pasien dengan Nomor {index} Tidak Ditemukan")
                        print()
                        menu_admin()
                        break
                else:
                    print()
                    print(">>> Input Harus Berupa Angka. Silakan Coba Lagi. <<<")
                    print()
                    menu_admin()
                    break

        elif tanya == "5":
            os.system('cls')
            ana.shell_sort()
            ana.tampilan_pasien()

        elif tanya == "6":
            os.system('cls')
            ana.shell_sort()
            ana.tampilan_pasien()
            ana.cari_pasien()

        elif tanya == "7":
            os.system('cls')
            login()
            break

        elif tanya == "8":
            os.system('cls')
            sys.exit(">>> Program Telah Selesai. <<<")

        else:
            print()
            print(">>> Pilihan Tidak Valid. Silakan Coba Lagi. <<<")
            print()
        
# Koneksi ke database
def koneksi():
    mydb = None
    try:
        mydb = mysql.connector.connect(
        host="db4free.net",
        user="joviana",
        password="kelompok66",
        database="kelompok6"
        )
        print(">>> Database Berhasil Dikonekkan <<<")
        print()
        print("SEDANG MEMPROSES....")
        time.sleep(3)
        os.system("cls")
        
    except mysql.connector.Error as e:
        print(f"Unconeccted Error: {e}")
    return mydb

# Fungsi registrasi pasien
def regis(mydb):
    cursor = mydb.cursor()

    while True:
        username = input("Masukkan Username Anda (hanya huruf): ").strip().lower()
        if not re.match("^[a-zA-Z]+$", username):
            print()
            print(">>> Username Hanya Boleh Menggunakan Huruf! <<<")
            print()
            login()
            return
        else:
            break

    while True:
        password = input("Masukkan Password Anda (hanya angka): ").strip()
        if not re.match("^[0-9]+$", password):
            print()
            print(">>> Password Hanya Boleh Menggunakan Angka! <<<")
            print()
            login()
            return
        else:
            break

    role = "pasien"

    # Query untuk memeriksa keberadaan username dan password di tabel user
    query = "INSERT INTO login (username, password, role) VALUES (%s, %s, %s)"
    values = (username, password, role)

    try:
        cursor.execute(query, values)
        mydb.commit()
    except Exception as e:
        print()
        print(">>> Terjadi Kesalahan: ", e)
        mydb.rollback()
        login()
        return

    # Jika ditemukan user dengan username dan password yang sesuai
    print()
    print(">>> Registrasi Berhasil. Anda Dapat Login Sebagai Pasien! <<<")
    print()
    login()
    return

# Fungsi login pasien   
def pasien_login():
    try:
        username = str.strip(input("Masukkan Username Pasien: ").replace (" ",""))
        password = pwinput.pwinput("Masukkan Password Pasien: ").strip("\t").strip(" ").replace("\t","")
        role = 'pasien'
        os.system('cls')

        # Query untuk memeriksa keberadaan username dan password di tabel user
        cursor = mydb.cursor()
        query = "SELECT * FROM login WHERE  username = %s AND password = %s AND role = %s"
        values = (username, password,role)
        cursor.execute(query, values)
        user = cursor.fetchone()

        # Jika ditemukan user dengan username yang sesuai
        if user:
            x = datetime.datetime.now()
            waktu = time.asctime( time.localtime(time.time()) )
            print("\t===========================================================")
            print("\tWelcome To Rumah Sakit Berjaya ", waktu)
            print("\t==========================================================\n")

            print("Login berhasil. Selamat datang, {}!".format(user[0]))
            time.sleep(3)
            os.system('cls')
            menu_pasien()
        else:
            print(">>> Maaf, Username atau Password yang Anda Masukkan Salah. <<<")
            print()
            login()
    except ValueError:
        print()
        print(">>> Maaf, Terjadi Kesalahan Pada Tipe Data yang Anda Masukkan. <<<")
        print()
        menu_pasien()
    
# Fungsi login admin
def admin_login():
    while True:
        try:
            username = str.strip(input("Masukkan Username Admin: ").replace (" ",""))
            password = pwinput.pwinput("Masukkan Password Admin: ").strip("\t").strip(" ").replace("\t","")
            role = 'admin'
            os.system('cls')
            
            # Query untuk memeriksa keberadaan username dan password di tabel admin
            cursor = mydb.cursor()
            query = "SELECT * FROM login WHERE  username = %s AND password = %s AND role = %s"
            values = (username, password, role)

            cursor.execute(query, values)

            admin = cursor.fetchone()

            if admin:
                x = datetime.datetime.now()
                waktu = time.asctime( time.localtime(time.time()) )
                print()
                print(waktu)
                print("Login berhasil. Selamat Datang, {}!".format(admin[0]))
                time.sleep(3)
                os.system('cls')
                menu_admin()
                break
            else:
                print()
                print(">>> Username dan Password yang Anda Masukkan Salah. Silakan Coba Lagi! <<<")
                print()
                login()
                break
            
        except ValueError:
            print()
            print(">>> Input Tidak Valid. Silakan Coba Lagi. <<<")
            print()
            menu_admin()
            break
            

mydb = koneksi()


# Main program
def login():
    ana.tambah_pasien("111", "jovi", 18, "kubar", "mag")
    ana.tambah_pasien("333", "fina", 19, "samarinda", "tifus")
    ana.tambah_pasien("222", "aufa", 19, "balikpapan", "demam")
    ana.tambah_pasien("444","young", 20, "jakarta", "dbd")
    ana.tambah_pasien("555", "alya", 21, "tengarong", "mag")
    
    print("|=================================|")
    print("|   SELAMAT DATANG DI MENU LOGIN  |")
    print("|            RS. BERJAYA          |")
    print("|=================================|")
    print()
    print("|=================================|")
    print("|========== PILIH OPSI ===========|")
    print("|=================================|")
    print("|====| 1.| Login Pasien           |")
    print("|====| 2.| Login Admin            |")
    print("|====| 3.| Registrasi Pasien Baru |")
    print("|====| 4.| Keluar                 |")
    print("|=================================|")
    print()   

# opsi pilihan menu    
def opsional():
    while True:
        try:               
            choice = input("Masukkan Pilihan: ")

            if choice == "1": 
                print()
                pasien_login()
                
            elif choice == "2":
                print()
                admin_login()
                
            elif choice == "3":
                print()
                regis(mydb)
                
            elif choice == "4":
                print()
                print(">>> TERIMA KASIH TELAH BERKUNJUNG DI RS BERJAYA <<<")
                exit()
            else:
                print()
                print(">>> Pilihan Tidak Valid. Silakan Coba Lagi. <<<")
                print()
                login()   
        except ValueError and KeyboardInterrupt:
            print (">>> Masukan Pilihan yang Sesuai! <<<")
        
login()
opsional()
