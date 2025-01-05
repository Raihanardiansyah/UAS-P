# UAS-PEMROGRAMAN

## Program Sederhana : Aplikasi Pengola Data Mahasiswa   
![Gambar1](https://github.com/Raihanardiansyah/UAS-P/blob/main/ss/Screenshot%202025-01-06%20055706.png?raw=true)   
### Yang Pertama ada Class Data   
ClassData, Kelas ini bertugas untuk menyimpan data mahasiswa. Data mahasiswa disimpan dalam bentuk list, di mana setiap elemen list adalah sebuah dictionary yang berisi nama dan nilai mahasiswa.   
Metode dalam ClassData:   
- __init__(self):
Konstruktor yang akan dipanggil saat objek dibuat. Metode ini menginisialisasi atribut data_mahasiswa sebagai list kosong.   
- __tambah_data__(self, nama, nilai):   
Metode ini digunakan untuk menambahkan data mahasiswa ke dalam list data_mahasiswa. Data disimpan dalam bentuk dictionary dengan kunci nama dan nilai.   
- __get_data__(self):   
Metode ini mengembalikan seluruh data mahasiswa yang telah disimpan dalam list data_mahasiswa.   

![Gambar2](https://github.com/Raihanardiansyah/UAS-P/blob/main/ss/Screenshot%202025-01-06%20055715.png?raw=true)   
### Dan Juga Yang Kedua ada Yang Namanya Classview   
ClassView, Kelas ini bertanggung jawab untuk menampilkan data mahasiswa dalam bentuk tabel yang rapi. Jika data kosong, maka akan ditampilkan pesan bahwa tidak ada data yang bisa ditampilkan.   
### Metode dalam ClassView:   
- __tampilkan_data__ (data):
Metode ini menerima parameter data, yang merupakan list dari data mahasiswa.
Metode ini akan mencetak tabel dengan tiga kolom: nomor urut, nama mahasiswa, dan nilai mahasiswa. Jika list kosong, maka akan ditampilkan pesan __“Tidak ada data untuk ditampilkan.”__

![Gambar3](https://github.com/Raihanardiansyah/UAS-P/blob/main/ss/Screenshot%202025-01-06%20055725.png?raw=true)
### Selanjutnya Ada ClassProcess   
ClassProcess, Kelas ini bertugas untuk memproses input dari pengguna dan melakukan validasi input. Validasi ini sangat penting agar data yang dimasukkan oleh pengguna benar dan sesuai dengan ketentuan.   
### Metode dalam ClassProcess:
- __init__(self, data_obj):   
Konstruktor ini menerima parameter data_obj, yaitu sebuah objek dari ClassData yang akan digunakan untuk menyimpan data mahasiswa.   
- __input_data__(self):   
Metode ini digunakan untuk meminta input dari pengguna berupa nama dan nilai mahasiswa.   
### Validasi dilakukan sebagai berikut:   
1. Nama tidak boleh kosong. Jika nama kosong, program akan menampilkan pesan “Nama tidak boleh kosong!” dan meminta input ulang.   
2. Nilai harus berupa angka di antara 0 hingga 100. Jika nilai tidak memenuhi syarat ini, program akan menampilkan pesan “Nilai harus berupa angka antara 0-100!” dan meminta input ulang.

![Gambar4](https://github.com/Raihanardiansyah/UAS-P/blob/main/ss/Screenshot%202025-01-06%20055739.png?raw=true)   
![Gambar5](https://github.com/Raihanardiansyah/UAS-P/blob/main/ss/Screenshot%202025-01-06%20055957.png?raw=true)   
### Dan Yang Terakhir adalah hasil   
### Penjelasan Alur Program
1. Membuat objek dari setiap kelas:   
- Objek data dibuat dari ClassData untuk menyimpan data mahasiswa.   
- Objek proses dibuat dari ClassProcess dengan parameter data untuk memproses input dan menyimpan hasilnya.   
- Objek view dibuat dari ClassView untuk menampilkan hasil akhir.   
2. Memproses input pengguna:   
- Program memanggil metode input_data dari objek proses, yang meminta pengguna untuk memasukkan nama dan nilai mahasiswa.   
- Jika pengguna memasukkan data yang tidak valid, program akan menampilkan pesan error dan meminta input ulang hingga data benar.   
3. Menampilkan data dalam bentuk tabel:   
- Setelah semua input dimasukkan, program memanggil metode tampilkan_data dari objek view, yang menampilkan data mahasiswa dalam bentuk tabel.

### Fitur Validasi Input   
1. Program ini dilengkapi dengan validasi input menggunakan exception handling untuk memastikan data yang dimasukkan benar. Berikut adalah validasi yang dilakukan:   
- Nama tidak boleh kosong   
Jika pengguna memasukkan nama kosong, program akan menampilkan pesan “Nama tidak boleh kosong!” dan meminta pengguna untuk mengulang input.   
- Nilai harus berupa angka di antara 0 hingga 100   
Jika pengguna memasukkan nilai di luar rentang 0 hingga 100 atau bukan angka, program akan menampilkan pesan “Nilai harus berupa angka antara 0-100!” dan meminta pengguna untuk mengulang input.   
Validasi ini sangat penting untuk menjaga agar data yang disimpan selalu benar dan tidak ada kesalahan.

### Kesimpulan
Program ini telah memenuhi semua ketentuan yang diminta, yaitu:   
1. Modular dan OOP: Program dirancang menggunakan tiga kelas terpisah yang bertanggung jawab atas fungsinya masing-masing.   
2. Meminta input dari pengguna: Program meminta pengguna untuk memasukkan nama dan nilai mahasiswa.   
3. Validasi input: Program memeriksa apakah input valid menggunakan exception handling.   
4. Menampilkan hasil dalam bentuk tabel: Data mahasiswa ditampilkan dalam bentuk tabel yang rapi menggunakan metode tampilkan_data dari ClassView.   
Dengan pendekatan ini, program tidak hanya sederhana tetapi juga modular, mudah dipahami, dan mudah dikembangkan lebih lanjut.   
