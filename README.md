# Projek-Akhir-Rumah-Sakit
Kelompok 6 Projek Akhir ASD Rumah Sakit

	Rumah sakit adalah sebuah institusi medis yang menyediakan perawatan kesehatan bagi pasien yang membutuhkan. Sebagai sebuah institusi yang memiliki tugas penting dalam menyelamatkan nyawa pasien, rumah sakit memerlukan pengelolaan data yang efektif dan efisien. Untuk itu, pemrograman mata kuliah algoritma dan struktur data sangatlah penting untuk diterapkan dalam pengelolaan data di rumah sakit.
	Contoh penerapan algoritma dan struktur data di rumah sakit adalah dalam sistem pencatatan medis elektronik (Electronic Medical Record/EMR). EMR adalah sebuah sistem yang digunakan untuk mengelola dan menyimpan data pasien secara digital. EMR menggunakan algoritma untuk mencari data pasien yang terkait dengan penyakit tertentu. EMR juga menggunakan struktur data seperti linked list untuk menyimpan data pasien secara efisien dan mempercepat proses pencarian data.
	Program Python untuk simulasi manajemen pasien pada sebuah rumah sakit dapat dibangun dengan menggunakan struktur data yang sesuai dan algoritma yang efektif. Dalam program tersebut, kita dapat menggunakan kelas sebagai wadah untuk menyimpan data dan metode-metode yang terkait.
	Program yang kami buat ini adalah sebuah program rumah sakit yang berfungsi untuk melakukan login pasien, login admin, dan registrasi pasien, yang dimana didalam menu-menu tersebut nantinya kan ada banyak menu pilihan lain lagi. Penjelasan lebih detail seperti dibawah ini.

STRUKTUR DATA : 
	Program dimulai dengan mengimpor beberapa modul dan memuat beberapa variabel yang akan digunakan dalam program. Pada tampilan awal akan tampil menu pilihan seperti Login Pasien, Login Admin, Registrasi Pasien, dan menu untuk keluar, seperti pada gambar dibawah ini.






1. Registrasi Pasien
Pada menu ini user akan diminta untuk menginputkan username beserta password untuk login pasien nantinya. Setelah itu program akan kembali ke menu sebelumnya.
 


2. Login Pasien
Pada menu ini user akan di arahkan untuk menginputkan username serta password pasien yang bersangkutan (password akan dilindungi, sehingga ketika menginputkan password, akan tampil simbol bintang saja). 
 

Dan jika berhasil login (data pasien ditemukan) maka program akan menampilkan pilihan menu lagi yakni informasi kamar, pemesanan, apotek, liat saldo, tambah saldo, dan exit.
 

 
1. Informasi Kamar
Sesuai namanya, pada menu ini program akan menampilkan informasi kamar yang tersdia pada Rumah Sakit Berjaya. Jika ingin keluar dari ini, pengguna dapat mengklik tombol “0” dan enter, dn program akan kembali ke menu sebelumnya.
    

2. Pemesanan
Dalam menu ini, user akan diarahkan untuk memesan kamar. Kemudian user diminta menginputkan id pasien yang telah terdaftar, nomor jenis kamar yang diinginkan dan jumlah hari untuk menginap. Setelah itu akan tampil sebuah invoice tentang informasi pemesanan kamar.
    

3. Apotek
Dalam menu ini, program akan memunculkan daftar obat yang tersedia pada rumah sakit tersebut. Setelah itu, user diminta untuk menginputkan nama serta jumlah obat yang ingin dibeli. Lalu akan muncul total harga dari obat yang akan dibeli.
 
4. Liat Saldo
Pada menu ini, user dapat melihat berapa jumlah saldo yang mereka miliki yang kemudian nantinya akan digunakan untuk membayar akses rumah sakit seperti kamar, biaya berobat, biaya obat, dll.

5. Tambah saldo
Pada menu ini, user dapat menambahkan saldo mereka miliki yang kemudian nantinya akan digunakan untuk membayar akses rumah sakit seperti kamar, biaya berobat, biaya obat, dll.

3. Login Admin
Sama seperti menu login pasien, pada menu login admin user juga akan diminta untuk menginputkan username dan password sebagai admin.
 

Lalu, program akan menampilkan menu pilihan lagi seperti registrasi pasien, read data pemeriksaan pasien, update data pasien, delete data pasien, sorting data pasien, searching data pasien, dll. Dan user akan diminta menginputkan menu apa yang ingin dijalankan.
 

1. Registrasi Pasien
Sama halnya seperti menu registrasi pasien pada menu awal program, menu ini juga bertujuan untuk membuat data pasien rumah sakit. Bedanya, pada menu ini, user diminta untuk menginputkan id, nama, umur, alamat, dan penyakit yang didiagnosa pasien.
 

2. Read Data Pemeriksaan Pasien
Pada menu ini program akan menampilkan data-data pasien yang sudah terdaftar sebelumnya.
 

3. Update Data Pasien
Pada menu ini user dapat mengubah data pasien yang sudah terdaftar. User akan diminta untuk menginputkan nomor data pasien yang akan di ubah. Setelah itu user diminta lagi untuk menginputkan perubahan data pasien seperti ID, nama, umur, alamat, dan penyakit yang di diagnosa.
 

4. Delete Data Pasien
Pada menu ini, user akan dapat menghapus data pasien yang telah terdaftar. User akan diminta untuk menginputkan nomor urut dari data pasien yang ingin dihapus.
 

5. Sorting Data Pasien
Pada menu ini user dapat mengurutkan data pasien yang telah terdaftar. Seperti pada gambar dibawah.
 

6. Searching Data Pasien
Pada menu ini user dapat mencari data pasien yang telah terdaftar. User akan diminta untuk menginputkan id pasien yang ingin dicari. Kemudian akan muncul data pasien yang dicari seperti indexnya, ID, nama, umur, alamat, dan diagnosa penyakit pasien.
 

