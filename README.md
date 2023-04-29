# Nama Kelompok
1. Joviana Young (2209116012)
2. Aufa Tri Hapsari (2209116031)
3. Fina Anriani (2209116051)


# Rumah-Sakit
Kelompok 6 Projek Akhir ASD Rumah Sakit


#Deskripsi Program
Rumah sakit adalah sebuah institusi medis yang menyediakan perawatan kesehatan bagi pasien yang membutuhkan. Sebagai sebuah institusi yang memiliki tugas penting dalam menyelamatkan nyawa pasien, rumah sakit memerlukan pengelolaan data yang efektif dan efisien. Untuk itu, pemrograman mata kuliah algoritma dan struktur data sangatlah penting untuk diterapkan dalam pengelolaan data di rumah sakit.
	
Contoh penerapan algoritma dan struktur data di rumah sakit adalah dalam sistem pencatatan medis elektronik (Electronic Medical Record/EMR). EMR adalah sebuah sistem yang digunakan untuk mengelola dan menyimpan data pasien secara digital. EMR menggunakan algoritma untuk mencari data pasien yang terkait dengan penyakit tertentu. EMR juga menggunakan struktur data seperti linked list untuk menyimpan data pasien secara efisien dan mempercepat proses pencarian data.
	
Program Python untuk simulasi manajemen pasien pada sebuah rumah sakit dapat dibangun dengan menggunakan struktur data yang sesuai dan algoritma yang efektif. Dalam program tersebut, kita dapat menggunakan kelas sebagai wadah untuk menyimpan data dan metode-metode yang terkait.
	
Program yang kami buat ini adalah sebuah program rumah sakit yang berfungsi untuk melakukan login pasien, login admin, dan registrasi pasien, yang dimana didalam menu-menu tersebut nantinya akan ada banyak menu pilihan lain lagi. Penjelasan lebih detail seperti dibawah ini.

# STRUKTUR PROJECT : 
- Sorting : Shell sort adalah salah satu algoritma pengurutan (sorting algorithm) yang digunakan untuk mengurutkan elemen dalam suatu array.

Dalam kode yang diberikan, terdapat fungsi shell_sort yang digunakan untuk mengurutkan elemen dalam suatu linked list. Algoritma shell sort ini mengurutkan elemen berdasarkan nilai ID pasien secara ascending (dari yang terkecil ke yang terbesar).

Pertama, program menentukan panjang linked list dengan menggunakan fungsi get_length(). Selanjutnya, program menentukan nilai gap yang digunakan dalam proses pengurutan. Gap ini awalnya diisi dengan setengah dari panjang linked list, dan kemudian diubah menjadi setengah dari gap sebelumnya dalam setiap iterasi.

- Searching : Jump Search merupakan salah satu strategi dalam algoritma pencarian (searching algorithm). Algoritma ini digunakan untuk mencari nilai tertentu dalam suatu array yang diurutkan. Algoritma Jump Search dilakukan pada suatu linked list yang berisi data pasien. Proses pencarian dimulai dengan menginisialisasi dua pointer yaitu left dan right, dimana left menunjuk ke indeks pertama dari linked list dan right ditentukan dengan menggunakan teknik jump.

Setelah itu, program memeriksa elemen pada indeks right. Jika nilai elemen ini kurang dari nilai yang dicari, maka pointer left dipindahkan ke indeks right dan pointer right diubah menjadi indeks berikutnya dengan teknik jump. Proses ini dilakukan terus-menerus sampai nilai elemen yang ditunjuk oleh pointer right lebih besar atau sama dengan nilai yang dicari.

Setelah menemukan range indeks yang memuat nilai yang dicari, program melakukan iterasi pada seluruh elemen pada range ini untuk mencari elemen yang sama dengan nilai yang dicari. Jika ditemukan, maka program akan menampilkan atribut-atribut dari elemen tersebut. Jika tidak ditemukan, program akan menampilkan pesan kesalahan.

1. Menu utama: tampilan menu yang digunakan untuk mengakses beberapa opsi yang tersedia dalam program. Menu ini bertujuan untuk memberikan kemudahan bagi pengguna untuk memilih opsi yang diinginkan. Pada bagian bawah menu, terdapat beberapa opsi yang dapat dipilih oleh pengguna, yaitu:

- Login Pasien: digunakan oleh pasien untuk melakukan login ke akun mereka pada sistem.
- Login Admin: digunakan oleh admin untuk melakukan login ke akun mereka pada sistem.
- Registrasi Pasien Baru: digunakan oleh pasien yang belum memiliki akun pada sistem untuk melakukan registrasi.
- Keluar: digunakan untuk keluar dari menu atau keluar dari sistem.

Setelah pengguna memilih salah satu opsi yang tersedia, program akan melakukan tindakan sesuai dengan opsi yang dipilih. Misalnya, jika pengguna memilih opsi "Login Pasien", program akan meminta pengguna untuk memasukkan informasi login mereka, yaitu username dan password. Setelah informasi login tersebut dimasukkan, program akan memverifikasi informasi tersebut dan memberikan akses pada pengguna untuk lanjut pada menu program yang selanjutnya.



#FITUR & FUNGSIONALITAS
Program dimulai dengan mengimpor beberapa modul dan memuat beberapa variabel yang akan digunakan dalam program. Pada tampilan awal akan tampil menu pilihan seperti Login Pasien, Login Admin, Registrasi Pasien, dan menu untuk keluar, seperti pada gambar dibawah ini.
	
![1](https://user-images.githubusercontent.com/127528115/232368480-555ea636-4841-4256-9580-23ff23677083.jpg)

(1). Registrasi Pasien

Pada menu ini user akan diminta untuk menginputkan username beserta password untuk login pasien nantinya. Setelah itu program akan kembali ke menu sebelumnya.

![2](https://user-images.githubusercontent.com/127528115/232368671-e99d5045-9742-478f-956a-d3144364cb20.jpg)

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

Sama seperti menu login pasien, pada menu login admin user juga akan diminta untuk menginputkan username dan password sebagai admin.

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
