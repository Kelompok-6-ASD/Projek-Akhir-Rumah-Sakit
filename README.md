# Rumah-Sakit
Kelompok 6 Projek Akhir ASD Rumah Sakit

Rumah sakit adalah sebuah institusi medis yang menyediakan perawatan kesehatan bagi pasien yang membutuhkan. Sebagai sebuah institusi yang memiliki tugas penting dalam menyelamatkan nyawa pasien, rumah sakit memerlukan pengelolaan data yang efektif dan efisien. Untuk itu, pemrograman mata kuliah algoritma dan struktur data sangatlah penting untuk diterapkan dalam pengelolaan data di rumah sakit.
	
Contoh penerapan algoritma dan struktur data di rumah sakit adalah dalam sistem pencatatan medis elektronik (Electronic Medical Record/EMR). EMR adalah sebuah sistem yang digunakan untuk mengelola dan menyimpan data pasien secara digital. EMR menggunakan algoritma untuk mencari data pasien yang terkait dengan penyakit tertentu. EMR juga menggunakan struktur data seperti linked list untuk menyimpan data pasien secara efisien dan mempercepat proses pencarian data.
	
Program Python untuk simulasi manajemen pasien pada sebuah rumah sakit dapat dibangun dengan menggunakan struktur data yang sesuai dan algoritma yang efektif. Dalam program tersebut, kita dapat menggunakan kelas sebagai wadah untuk menyimpan data dan metode-metode yang terkait.
	
Program yang kami buat ini adalah sebuah program rumah sakit yang berfungsi untuk melakukan login pasien, login admin, dan registrasi pasien, yang dimana didalam menu-menu tersebut nantinya kan ada banyak menu pilihan lain lagi. Penjelasan lebih detail seperti dibawah ini.

STRUKTUR DATA : 

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

![5](https://user-images.githubusercontent.com/127528115/232368833-e0534311-c24c-4d29-9b4b-f2b005156475.jpg)

1. Informasi Kamar

	Sesuai namanya, pada menu ini program akan menampilkan informasi kamar yang tersdia pada Rumah Sakit Berjaya. Jika ingin keluar dari ini, pengguna dapat mengklik tombol “0” dan enter, dn program akan kembali ke menu sebelumnya.

![6](https://user-images.githubusercontent.com/127528115/232368881-a08a73e8-bfcc-4342-a370-aaff1e4c1091.jpg)

![7](https://user-images.githubusercontent.com/127528115/232368937-dec856d7-b117-46d0-af3a-369f6922bbc9.jpg)

2. Pemesanan

	Dalam menu ini, user akan diarahkan untuk memesan kamar. Kemudian user diminta menginputkan id pasien yang telah terdaftar, nomor jenis kamar yang diinginkan dan jumlah hari untuk menginap. Setelah itu akan tampil sebuah invoice tentang informasi pemesanan kamar.

![8](https://user-images.githubusercontent.com/127528115/232369043-05554c3b-a42a-4802-afa9-b13874a05647.jpg)

![9](https://user-images.githubusercontent.com/127528115/232369082-9b249768-0c61-430f-8d09-e432ce7679a7.jpg)

![10](https://user-images.githubusercontent.com/127528115/232369112-9b2765a1-3052-4f1d-aac0-66e204b6d237.jpg)

3. Apotek

	Dalam menu ini, program akan memunculkan daftar obat yang tersedia pada rumah sakit tersebut. Setelah itu, user diminta untuk menginputkan nama serta jumlah obat yang ingin dibeli. Lalu akan muncul total harga dari obat yang akan dibeli.

![11](https://user-images.githubusercontent.com/127528115/232369198-4520bc0f-10b7-4c0c-9c6b-aa090037d275.jpg)

4. Liat Saldo

	Pada menu ini, user dapat melihat berapa jumlah saldo yang mereka miliki yang kemudian nantinya akan digunakan untuk membayar akses rumah sakit seperti kamar, biaya berobat, biaya obat, dll.

![lihat saldo](https://user-images.githubusercontent.com/127528115/233644794-33230a53-05c0-451f-b3fc-7666bc903ef6.PNG)

5. Tambah saldo

	Pada menu ini, user dapat menambahkan saldo mereka miliki yang kemudian nantinya akan digunakan untuk membayar akses rumah sakit seperti kamar, biaya berobat, biaya obat, dll.

![tambah saldo](https://user-images.githubusercontent.com/127528115/233644854-3883c2fa-6ccd-42d0-bc58-2e43f354cff1.PNG)


(3). Login Admin

Sama seperti menu login pasien, pada menu login admin user juga akan diminta untuk menginputkan username dan password sebagai admin.

![12](https://user-images.githubusercontent.com/127528115/232369334-0e62b537-e2e6-4145-8460-c44739b872fe.jpg)

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
