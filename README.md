# Nama Kelompok
1. Joviana Young (2209116012)
2. Aufa Tri Hapsari (2209116031)
3. Fina Anriani (2209116051)


# Rumah-Sakit
Kelompok 6 Projek Akhir ASD Rumah Sakit


# Deskripsi Program
Rumah sakit adalah sebuah institusi medis yang menyediakan perawatan kesehatan bagi pasien yang membutuhkan. Sebagai sebuah institusi yang memiliki tugas penting dalam menyelamatkan nyawa pasien, rumah sakit memerlukan pengelolaan data yang efektif dan efisien. Untuk itu, pemrograman mata kuliah algoritma dan struktur data sangatlah penting untuk diterapkan dalam pengelolaan data di rumah sakit.
	
Contoh penerapan algoritma dan struktur data di rumah sakit adalah dalam sistem pencatatan medis elektronik (Electronic Medical Record/EMR). EMR adalah sebuah sistem yang digunakan untuk mengelola dan menyimpan data pasien secara digital. EMR menggunakan algoritma untuk mencari data pasien yang terkait dengan penyakit tertentu. EMR juga menggunakan struktur data seperti linked list untuk menyimpan data pasien secara efisien dan mempercepat proses pencarian data.
	
Program Python untuk simulasi manajemen pasien pada sebuah rumah sakit dapat dibangun dengan menggunakan struktur data yang sesuai dan algoritma yang efektif. Dalam program tersebut, kita dapat menggunakan kelas sebagai wadah untuk menyimpan data dan metode-metode yang terkait.
	
Program yang kami buat ini adalah sebuah program rumah sakit yang berfungsi untuk melakukan login pasien, login admin, dan registrasi pasien, yang dimana didalam menu-menu tersebut nantinya akan ada banyak menu pilihan lain lagi. Penjelasan lebih detail seperti dibawah ini.

# STRUKTUR PROJECT : 
- Modul-modul yang digunakan, antara lain :

mysql.connector: Modul ini digunakan untuk menghubungkan Python dengan database MySQL. 

pwinput: Modul ini digunakan untuk mengambil masukan kata sandi dari pengguna secara aman, sehingga sandi tidak akan terlihat saat dimasukkan.

math: Modul ini menyediakan fungsi-fungsi matematika dasar seperti fungsi trigonometri, logaritma, dan fungsi untuk menghitung akar kuadrat.

prettytable: Modul ini digunakan untuk membuat tabel dengan format yang rapi dan mudah dibaca.

time: Modul ini menyediakan fungsi-fungsi untuk memanipulasi waktu, seperti mengambil waktu saat ini, menunda program, atau menghitung waktu yang diperlukan untuk menjalankan suatu fungsi.

datetime: Modul ini digunakan untuk memanipulasi tanggal dan waktu dalam berbagai format, seperti mengambil waktu saat ini, mengubah format waktu, atau melakukan operasi pada tanggal dan waktu.

sys: Modul ini menyediakan akses ke beberapa variabel dan fungsi sistem yang terkait dengan interpretasi Python, seperti variabel argv, exit(), dan path.

termcolor: Modul ini digunakan untuk menambahkan warna pada output teks pada konsol, sehingga memudahkan pembacaan dan memperindah tampilan output.

os: Modul ini digunakan untuk melakukan operasi pada sistem operasi yang digunakan.

- Class : Class Pasien adalah class yang digunakan untuk mendefinisikan objek Pasien, dengan atribut id_pasien, nama_pasien, umur_pasien, alamat, dan diagnosa. Selain itu, terdapat juga atribut next yang akan digunakan untuk menyimpan referensi ke objek Pasien berikutnya dalam linked list. Class Pasien juga memiliki metode konstruktor __init__, yang digunakan untuk menginisialisasi nilai dari atribut-atribut objek Pasien. Class LinkedList adalah class yang digunakan untuk membuat linked list, yaitu sebuah struktur data yang terdiri dari sejumlah node yang saling terhubung. Pada class ini, terdapat dua atribut, yaitu head dan saldo. Atribut head akan digunakan untuk menyimpan referensi ke node pertama dalam linked list, sedangkan atribut saldo akan digunakan untuk menyimpan nilai saldo awal dari linked list. Class LinkedList juga memiliki metode konstruktor __init__, yang digunakan untuk menginisialisasi nilai dari atribut-atribut objek LinkedList.
Class Pasien akan digunakan untuk membuat objek-objek Pasien yang akan dimasukkan ke dalam linked list yang dibuat menggunakan class LinkedList. Setiap objek Pasien akan menjadi satu node dalam linked list, dan atribut next dari objek Pasien akan digunakan untuk menyimpan referensi ke objek Pasien berikutnya dalam linked list. Dengan demikian, class Pasien dan LinkedList akan bekerja bersama-sama untuk membentuk struktur data linked list yang digunakan untuk menyimpan objek Pasien.

- Sorting : Shell sort adalah salah satu algoritma pengurutan (sorting algorithm) yang digunakan untuk mengurutkan elemen dalam suatu array. Fungsi shell_sort yang digunakan untuk mengurutkan elemen dalam suatu linked list. 

- Searching : Jump Search merupakan salah satu strategi dalam algoritma pencarian (searching algorithm). Proses pencarian dimulai dengan menginisialisasi dua pointer yaitu left dan right, dimana left menunjuk ke indeks pertama dari linked list dan right ditentukan dengan menggunakan teknik jump.Setelah itu, program memeriksa elemen pada indeks right. Jika nilai elemen ini kurang dari nilai yang dicari, maka pointer left dipindahkan ke indeks right dan pointer right diubah  menjadi indeks berikutnya dengan teknik jump. Proses ini dilakukan terus-menerus sampai nilai elemen yang ditunjuk oleh pointer right lebih besar atau sama dengan nilai yang dicari. Setelah menemukan range indeks yang memuat nilai yang dicari, program melakukan iterasi pada seluruh elemen pada range ini untuk mencari elemen yang sama dengan nilai yang dicari. Jika ditemukan, maka program akan menampilkan atribut-atribut dari elemen tersebut. Jika tidak ditemukan, program akan menampilkan pesan kesalahan.

- Inisialisasi Class :
ana = LinkedList()
Ini adalah inisialisasi objek dari kelas LinkedList dengan nama ana. Setelah objek ana dibuat, ana memiliki atribut head dan saldo yang telah diinisialisasi dengan nilai None dan 1000000000, masing-masing.

1. Menu utama: tampilan menu yang digunakan untuk mengakses beberapa opsi yang tersedia dalam program. Menu ini bertujuan untuk memberikan kemudahan bagi pengguna untuk memilih opsi yang diinginkan. Pada bagian bawah menu, terdapat beberapa opsi yang dapat dipilih oleh pengguna, yaitu:

- Login Pasien: digunakan oleh pasien untuk melakukan login ke akun mereka pada sistem.
- Login Admin: digunakan oleh admin untuk melakukan login ke akun mereka pada sistem.
- Registrasi Pasien Baru: digunakan oleh pasien yang belum memiliki akun pada sistem untuk melakukan registrasi.
- Keluar: digunakan untuk keluar dari menu atau keluar dari sistem.

Setelah pengguna memilih salah satu opsi yang tersedia, program akan melakukan tindakan sesuai dengan opsi yang dipilih. Misalnya, jika pengguna memilih opsi "Login Pasien", program akan meminta pengguna untuk memasukkan informasi login mereka, yaitu username dan password. Setelah informasi login tersebut dimasukkan, program akan memverifikasi informasi tersebut dan memberikan akses pada pengguna untuk lanjut pada menu program yang selanjutnya.

2. Menu login
Fungsi pasien_login() bertanggung jawab untuk melakukan proses login pasien. Pertama-tama, fungsi ini akan meminta input username dan password dari pengguna. Kemudian, fungsi ini akan melakukan query ke database untuk memeriksa apakah username dan password yang dimasukkan sesuai dengan data yang ada di database. Jika username dan password ditemukan, maka pengguna akan diberikan akses ke menu_pasien(). Jika tidak ditemukan, maka pengguna akan diminta untuk memasukkan kembali username dan password yang benar.

Fungsi admin_login() juga melakukan proses login, namun untuk akun admin. Fungsi ini meminta input username dan password dari pengguna dan melakukan query ke database untuk memeriksa apakah data tersebut valid. Jika ditemukan akun admin yang sesuai, pengguna akan diberikan akses ke menu_admin(). Jika tidak ditemukan, pengguna akan diminta untuk memasukkan kembali username dan password yang benar.

3. Menu Register
Fungsi regis di atas merupakan sebuah fungsi yang bertujuan untuk melakukan registrasi user. Fungsi ini akan meminta input dari user berupa username dan password yang akan digunakan untuk login di aplikasi.


# FITUR & FUNGSIONALITAS
- Fitur yang pertama yaitu terdapat pada awal program, menu utama disini memiliki ke 3 fungsi yang pertama adalah pasien login, kemudian admin login, dan register

- Berikut ini fitur-fitur yang ada pada menu admin :
1.  Registrasi pasien/Create: Admin melalukan registrasi untuk pasien, fungsi ini digunakan untuk menambahkan data baru ke dalam database atau sumber daya lainnya. Pada kode program yang diberikan, fungsi ini terletak pada pilihan 1 dari menu admin, dimana data pasien baru ditambahkan ke dalam sistem.
2.  Read: Fungsi ini terletak pada pilihan 2 dari menu admin, dimana data pasien yang sudah tersimpan ditampilkan.
3.  Update: fungsi ini terletak pada pilihan 3 dari menu admin, dimana data pasien yang ingin diupdate dipilih dan kemudian data tersebut diubah dengan data baru.
4.  Delete: Fungsi ini terletak pada pilihan 4 dari menu admin, dimana data pasien yang ingin dihapus dipilih dan kemudian data tersebut dihapus dari sistem.
5.  Sorting : Melakukan sorting data pasien menggunakan metode shell sort. Algoritma shell sort ini mengurutkan elemen berdasarkan nilai ID pasien secara ascending (dari yang terkecil ke yang terbesar). Pertama, program menentukan panjang linked list dengan menggunakan fungsi get_length(). Selanjutnya, program menentukan nilai gap yang digunakan dalam proses pengurutan. Gap ini awalnya diisi dengan setengah dari panjang linked list, dan kemudian diubah menjadi setengah dari gap sebelumnya dalam setiap iterasi.
6.  Searching : Algoritma Jump Search dilakukan pada suatu linked list yang berisi data pasien.
7.  Keluar menu admin : Untuk keluar dari menu admin
8.  Exit : Untuk keluar dari sistem

- Berikut ini fitur-fitur yang ada pada menu Pasien :
1.  Informasi Kamar: Opsi ini memungkinkan pengguna untuk melihat informasi kamar yang ada pada rumah sakit.
2.  Pemesanan: Opsi ini memungkinkan pengguna untuk melakukan pemesanan kamar.
3.  Apotek: Opsi ini memungkinkan pasien untuk membeli obat yang tersedia di apotek.
4.  Liat Saldo: Opsi ini memungkinkan pasien untuk melihat saldo yang tersisa.
5.  Tambah Saldo: Opsi ini memungkinkan pengguna untuk menambah saldo yang dimiliki pasien agar dapat melakukan pembayaran untuk layanan atau produk kesehatan yang digunakan.
6.  Keluar Menu Pasien: Opsi ini memungkinkan pengguna untuk kembali menu sebelumnya dalam program.
7.  Exit: Opsi ini memungkinkan pengguna untuk keluar dari program.


# Cara Penggunaan Beserta Outputnya
Program dimulai dengan mengimpor beberapa modul dan memuat beberapa variabel yang akan digunakan dalam program. Pada tampilan awal akan tampil menu pilihan seperti Login Pasien, Login Admin, Registrasi Pasien, dan menu untuk keluar, seperti pada gambar dibawah ini.
	
![asd 12](https://user-images.githubusercontent.com/127528115/235316313-d1bd53aa-799d-4db0-a462-7437b2aa851b.PNG)

(1). Registrasi Pasien

Pada menu ini user akan diminta untuk menginputkan username beserta password untuk login pasien nantinya. Setelah itu program akan kembali ke menu sebelumnya.

![asd 14](https://user-images.githubusercontent.com/127528115/235316528-a6af9cef-71a8-4aa8-87da-bc08a23becaf.PNG)

(2). Login Pasien

Pada menu ini user akan di arahkan untuk menginputkan username serta password pasien yang bersangkutan (password akan dilindungi, sehingga ketika menginputkan password, akan tampil simbol bintang saja). 

![3](https://user-images.githubusercontent.com/127528115/232368738-a9f6d1fe-bd21-4269-a6ba-75387277de60.jpg)

Dan jika berhasil login (data pasien ditemukan) maka program akan menampilkan pilihan menu lagi yakni informasi kamar, pemesanan, apotek, liat saldo, tambah saldo, dan exit.

![4](https://user-images.githubusercontent.com/127528115/232368808-91c8ebe7-ba4e-4553-ad42-7d9a49a4635f.jpg)

![asd 6](https://user-images.githubusercontent.com/127528115/235312341-0ef4b7d3-8c0f-4021-a3ad-9d1917db27f2.PNG)

1. Informasi Kamar

	Sesuai namanya, pada menu ini program akan menampilkan informasi kamar yang tersdia pada Rumah Sakit Berjaya. Jika ingin keluar dari ini, pengguna dapat mengklik tombol “0” dan enter, dan program akan kembali ke menu sebelumnya.

![asd 7](https://user-images.githubusercontent.com/127528115/235312475-c6030865-dbdc-46e8-a846-a1fd49d2d725.PNG)

2. Pemesanan

	Dalam menu ini, user akan diarahkan untuk memesan kamar. Kemudian user diminta menginputkan id pasien yang telah terdaftar, nomor jenis kamar yang diinginkan dan jumlah hari untuk menginap. Setelah itu akan tampil sebuah invoice tentang informasi pemesanan kamar.

![asd 1](https://user-images.githubusercontent.com/127528115/235311934-7e56cebf-2c67-4071-919a-a3b1315d175e.PNG)

![asd 2](https://user-images.githubusercontent.com/127528115/235311958-051ae3d7-eec2-4ff6-948d-2e93da814536.PNG)

3. Apotek

	Dalam menu ini, program akan memunculkan daftar obat yang tersedia pada rumah sakit tersebut. Setelah itu, user diminta untuk menginputkan nama serta jumlah obat yang ingin dibeli. Lalu akan muncul total harga dari obat yang akan dibeli.

![asd 5](https://user-images.githubusercontent.com/127528115/235312153-cce2553f-0415-4cf6-9670-eef12175ad6b.PNG)

4. Lihat Saldo

	Pada menu ini, user dapat melihat berapa jumlah saldo yang mereka miliki yang kemudian nantinya akan digunakan untuk membayar akses rumah sakit seperti kamar, biaya berobat, biaya obat, dll.

![asd 8](https://user-images.githubusercontent.com/127528115/235312738-2ac3a183-d0a5-463c-b771-6b7477248bdb.PNG)

5. Tambah saldo

	Pada menu ini, user dapat menambahkan saldo mereka miliki yang kemudian nantinya akan digunakan untuk membayar akses rumah sakit seperti kamar, biaya berobat, biaya obat, dll.

![asd 9](https://user-images.githubusercontent.com/127528115/235312764-7a546bdf-8181-40ef-8696-015274029f90.PNG)

![asd 10](https://user-images.githubusercontent.com/127528115/235312785-9ba16cbf-6e13-47eb-a08d-3a001cea19a7.PNG)

(3). Login Admin

Sama seperti menu login pasien, pada menu login admin user juga akan diminta untuk menginputkan username dan password (password dilindungi sehingga hanya akan tampil simbol bintang saja) sebagai admin.

![asd 11](https://user-images.githubusercontent.com/127528115/235316139-3e7a4ad5-780c-4471-a16f-8916b96b3a7c.PNG)

![Screenshot (191)](https://user-images.githubusercontent.com/127528115/235316174-007dc400-ec08-4fc6-90d7-d3e498c808c9.png)

Lalu, program akan menampilkan menu pilihan lagi seperti registrasi pasien, read data pemeriksaan pasien, update data pasien, delete data pasien, sorting data pasien, searching data pasien, dll. Dan user akan diminta menginputkan menu apa yang ingin dijalankan.

![13](https://user-images.githubusercontent.com/127528115/232369387-fe3c1d3f-e586-453e-9538-8fa3564d3eba.jpg)

1. Registrasi Pasien

	Sama halnya seperti menu registrasi pasien pada menu awal program, menu ini juga bertujuan untuk membuat data pasien rumah sakit. Bedanya, pada menu ini, user diminta untuk menginputkan id, nama, umur, alamat, dan penyakit yang didiagnosa pasien.

![14](https://user-images.githubusercontent.com/127528115/232369461-aa223973-32a2-4ba9-8a94-651e49f22ad9.jpg)

2. Read Data Pemeriksaan Pasien

	Pada menu ini program akan menampilkan data-data pasien yang sudah terdaftar sebelumnya.

![15](https://user-images.githubusercontent.com/127528115/232369524-34f7a279-9252-4018-8fbc-5b14d935c3e1.jpg)

3. Update Data Pasien

	Pada menu ini user dapat mengubah data pasien yang sudah terdaftar. User akan diminta untuk menginputkan nomor data pasien yang akan di ubah. Setelah itu user diminta lagi untuk menginputkan perubahan data pasien seperti ID, nama, umur, alamat, dan penyakit yang di diagnosa.

![16](https://user-images.githubusercontent.com/127528115/232369572-c8b97cad-8599-491f-94f3-6021fbdb94dc.jpg)


4. Delete Data Pasien

	Pada menu ini, user akan dapat menghapus data pasien yang telah terdaftar. User akan diminta untuk menginputkan nomor urut dari data pasien yang ingin dihapus.

![17](https://user-images.githubusercontent.com/127528115/232369628-6dfbb411-87db-46ee-a7b3-d355eae1f560.jpg)

5. Sorting Data Pasien

	Pada menu ini user dapat mengurutkan data pasien yang telah terdaftar. Seperti pada gambar dibawah.

![18](https://user-images.githubusercontent.com/127528115/232369699-8ef34090-067b-487c-8fac-f1c4827d14ab.jpg)

6. Searching Data Pasien

	Pada menu ini user dapat mencari data pasien yang telah terdaftar. User akan diminta untuk menginputkan id pasien yang ingin dicari. Kemudian akan muncul data pasien yang dicari seperti indexnya, ID, nama, umur, alamat, dan diagnosa penyakit pasien.

![19](https://user-images.githubusercontent.com/127528115/232369741-7017f015-8b75-45a3-a448-e3740fb73145.jpg)
