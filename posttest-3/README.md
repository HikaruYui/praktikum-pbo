# Posttest 3 

## Deskripsi Program

Sistem Manajemen Keuangan merupakan aplikasi berbasis Python yang digunakan untuk mengelola dompet digital, mencatat pemasukan dan pengeluaran, serta menampilkan saldo dan riwayat transaksi.

Program ini dikembangkan menggunakan konsep **Object-Oriented Programming (OOP)**, dengan fokus pada penerapan **abstraksi, polimorfisme, relasi antarkelas, dan operator overloading**. Program juga menerapkan salah satu prinsip SOLID, yaitu **Open/Closed Principle (OCP)**.

## 1. Struktur Program

Program terdiri dari beberapa file utama:

| File | Fungsi |
|---|---|
| `user.py` | Mengelola data pengguna dan hubungan pengguna dengan dompet. |
| `dompet.py` | Mengelola saldo, pencatatan transaksi, dan riwayat transaksi. |
| `transaksi.py` | Mendefinisikan abstract class `Transaksi` beserta subclass `Pemasukan` dan `Pengeluaran`. |
| `laporan.py` | Menampilkan laporan saldo dan riwayat transaksi menggunakan konsep duck typing. |
| `main.py` | Menjalankan program dan menghubungkan seluruh class. |

## 2. Class Diagram dan Relasi UML

Class Diagram digunakan untuk menggambarkan struktur kelas dan hubungan antarkelas dalam program Sistem Manajemen Keuangan.

**Diagram UML:**

![Class Diagram Sistem Manajemen Keuangan](assets/class_diagram.png)

### 2.1 Asosiasi (Association)

**Relasi: `LaporanSaldo` — `Dompet` dan `LaporanRiwayat` — `Dompet`**

Relasi asosiasi diterapkan karena kedua class laporan menyimpan referensi objek `Dompet` melalui atribut `self.dompet` untuk mengakses informasi keuangan. Class laporan menggunakan data dompet tanpa bertanggung jawab membuat atau mengelola siklus hidup objek tersebut.

Implementasi terdapat pada constructor `__init__(self, dompet)` di file `laporan.py`.

### 2.2 Agregasi (Aggregation)

**Relasi: `User` ◇—— `Dompet`**

Relasi agregasi diterapkan karena satu `User` dapat memiliki beberapa objek `Dompet` yang dibuat secara terpisah. Objek `Dompet` tetap dapat digunakan secara independen meskipun tidak lagi terdaftar dalam daftar dompet milik `User`.

Implementasi terdapat pada method `tambah_dompet()` di file `user.py`, yang menyimpan objek dompet ke dalam `self.daftar_dompet`.

### 2.3 Komposisi (Composition)

**Relasi: `Dompet` ◆—— `Transaksi`**

Relasi komposisi digunakan untuk memodelkan transaksi sebagai bagian dari catatan keuangan suatu dompet. Dalam desain program, `Dompet` bertanggung jawab membuat, memvalidasi, dan mencatat transaksi melalui method `tambah_transaksi()`.

Implementasinya terdapat pada `dompet.py`, yaitu pembuatan objek menggunakan `kelas_transaksi(...)` dan penyimpanannya melalui `self.__daftar_transaksi.append(transaksi)`.

Hubungan ini merupakan komposisi berdasarkan tanggung jawab kepemilikan dalam desain aplikasi, bukan karena Python secara otomatis menghapus semua referensi objek transaksi ketika dompet dihapus.

## 3. Penerapan Abstraksi (Abstract Base Class)

Abstraksi diterapkan pada file `transaksi.py` dengan menggunakan modul `abc` dari Python.

Class `Transaksi` didefinisikan sebagai abstract class menggunakan `ABC`. Class ini berfungsi sebagai dasar bagi berbagai jenis transaksi dan menetapkan method yang wajib dimiliki setiap subclass.

### 3.1 Abstract Method

Class `Transaksi` memiliki dua abstract method:

1. `perubahan_saldo()` — menentukan nilai perubahan saldo berdasarkan jenis transaksi.
2. `tampilkan()` — menampilkan informasi transaksi.

Kedua method ditandai dengan dekorator `@abstractmethod`, sehingga setiap subclass konkret wajib menyediakan implementasinya.

### 3.2 Implementasi pada Subclass

Terdapat dua subclass yang mewarisi `Transaksi`:

**Class `Pemasukan`**

- Menggunakan `super().__init__()` untuk memanggil constructor class induk.
- Memiliki atribut khusus `sumber`.
- Method `perubahan_saldo()` mengembalikan nilai positif sehingga saldo bertambah.
- Method `tampilkan()` menampilkan informasi pemasukan beserta sumbernya.

**Class `Pengeluaran`**

- Menggunakan `super().__init__()` untuk memanggil constructor class induk.
- Memiliki atribut khusus `metode_pembayaran`.
- Method `perubahan_saldo()` mengembalikan nilai negatif sehingga saldo berkurang.
- Method `tampilkan()` menampilkan informasi pengeluaran beserta metode pembayarannya.

Dengan demikian, kedua subclass mengimplementasikan seluruh abstract method yang diwajibkan class induk.

### 3.3 Method Konkret

Selain abstract method, class `Transaksi` memiliki method konkret `ringkasan()`.

Method ini digunakan bersama oleh `Pemasukan` dan `Pengeluaran` untuk menghasilkan ringkasan informasi transaksi, seperti ID, kategori, tipe, dan perubahan saldo.

Method `ringkasan()` memanggil `self.perubahan_saldo()`, sehingga hasilnya menyesuaikan implementasi pada setiap subclass tanpa perlu menulis ulang method ringkasan.


## 4. Penerapan Polimorfisme

Polimorfisme memungkinkan objek yang berbeda merespons pemanggilan method yang sama dengan perilaku yang berbeda.

Program menerapkan polimorfisme melalui pewarisan dan duck typing.

### 4.1 Polimorfisme melalui Pewarisan (Method Overriding)

**Lokasi:** `transaksi.py` dan `main.py`

Polimorfisme melalui inheritance diterapkan pada subclass `Pemasukan` dan `Pengeluaran` yang melakukan overriding terhadap method `perubahan_saldo()` dan `tampilkan()`.

Method `perubahan_saldo()` memiliki perilaku berbeda:

- `Pemasukan` mengembalikan jumlah transaksi sebagai nilai positif.
- `Pengeluaran` mengembalikan jumlah transaksi sebagai nilai negatif.

Pada `main.py`, objek dari kedua subclass disimpan dalam daftar transaksi dan dipanggil menggunakan satu perulangan:

`for transaksi in d1.daftar_transaksi:`

Di dalam perulangan tersebut, program menjalankan `transaksi.tampilkan()` dan `transaksi.ringkasan()`.

Python akan menjalankan implementasi method berdasarkan objek yang sedang diproses. Dengan demikian, program tidak memerlukan pemeriksaan jenis transaksi menggunakan `type()` maupun rantai `if/elif`.

### 4.2 Duck Typing

**Lokasi:** `laporan.py` dan `main.py`

Duck typing diterapkan menggunakan dua class yang tidak memiliki hubungan pewarisan, yaitu:

- `LaporanSaldo`
- `LaporanRiwayat`

Kedua class memiliki method dengan nama yang sama, yaitu `cetak()`, tetapi menghasilkan keluaran yang berbeda.

`LaporanSaldo.cetak()` menampilkan tabel nama dompet dan saldo, sedangkan `LaporanRiwayat.cetak()` menampilkan tabel riwayat transaksi.

Kedua objek diproses menggunakan fungsi yang sama, yaitu `cetak_laporan(laporan)`, yang hanya memanggil `laporan.cetak()`.

Pada `main.py`, fungsi tersebut digunakan dalam satu perulangan yang berisi objek `LaporanSaldo` dan `LaporanRiwayat`.

Konsep ini menunjukkan bahwa Python dapat memanggil method berdasarkan kemampuan objek tanpa mengharuskan objek berasal dari class induk yang sama.

### 4.3 Operator Overloading

**Lokasi:** `dompet.py`

Operator overloading diterapkan melalui magic method `__str__()` pada class `Dompet`.

Method `__str__()` digunakan untuk mengatur representasi string suatu objek saat dipanggil menggunakan `str()` atau `print()`.

Sebagai contoh, objek dompet dapat ditampilkan dengan format:

`Dompet 'Dompet Utama' (saldo: Rp3,475,000)`

Dengan demikian, informasi objek lebih mudah dibaca dibandingkan representasi objek bawaan Python.

## 5. Penerapan Enkapsulasi dan Inheritance

Program tetap mempertahankan konsep inheritance dan enkapsulasi yang telah diterapkan pada posttest sebelumnya.

### 5.1 Inheritance

Class `Pemasukan` dan `Pengeluaran` mewarisi atribut dan method dari `Transaksi`.

Kedua subclass menggunakan `super().__init__(...)` untuk melakukan inisialisasi atribut dari class induk, serta menambahkan atribut unik sesuai kebutuhan masing-masing transaksi.

### 5.2 Protected dan Private Attribute

Contoh penerapan atribut protected dan private meliputi:

- `Transaksi._jumlah` = atribut protected untuk menyimpan nominal transaksi.
- `Transaksi.__id_transaksi` = atribut private untuk menyimpan ID transaksi.
- `Dompet.__saldo` = atribut private untuk menyimpan saldo.
- `Dompet.__daftar_transaksi` = atribut private untuk menyimpan riwayat transaksi.
- `User.__password` = atribut private untuk menyimpan data password pada simulasi OOP.

Akses terhadap beberapa atribut tersebut dikendalikan menggunakan `@property` dan setter.

Sebagai contoh, setter `jumlah` menolak nominal transaksi yang tidak lebih besar dari nol, sedangkan setter `saldo` menolak nilai saldo negatif.

## 6. Penerapan Prinsip SOLID (Nilai Tambahan)

### Open/Closed Principle (OCP)

**Lokasi:** `dompet.py`, pada method `tambah_transaksi()`.

Open/Closed Principle menyatakan bahwa komponen perangkat lunak sebaiknya terbuka untuk pengembangan, tetapi tidak memerlukan perubahan pada logika yang sudah ada ketika fitur baru ditambahkan.

Pada program ini, method `tambah_transaksi()` menerima class transaksi melalui parameter `kelas_transaksi`.

Setelah objek dibuat, method memanggil `transaksi.perubahan_saldo()` untuk menentukan perubahan saldo tanpa memeriksa apakah transaksi tersebut termasuk pemasukan atau pengeluaran.

Sebagai contoh pengembangan, dapat ditambahkan subclass baru bernama `Cashback` yang mewarisi `Transaksi` dan mengimplementasikan seluruh abstract method.

Objek `Cashback` dapat diproses melalui `tambah_transaksi()` tanpa perlu mengubah logika utama pencatatan pada class `Dompet`, selama constructor dan perilakunya mengikuti kontrak yang digunakan method tersebut.

Dengan demikian, penerapan OCP memungkinkan pengembangan jenis transaksi baru secara lebih fleksibel dan mengurangi kebutuhan modifikasi pada kode yang telah ada.

## 7. Hasil Eksekusi Program

Program dijalankan melalui file `main.py`, yang menghubungkan objek pengguna, dompet, transaksi, serta laporan keuangan.

Output utama menampilkan profil pengguna dan saldo, informasi pemasukan serta pengeluaran, dan laporan keuangan dalam bentuk tabel.

**Screenshot output program:**

![Output Program](assets/output_program.png)

### Bukti Pengujian Abstraksi

Hasil `TypeError` membuktikan bahwa class `Transaksi` tidak dapat diinstansiasi secara langsung.

Output Bukti Abstraksi: 

## 8. Cara Menjalankan Program

Pastikan Python dan library `tabulate` sudah terpasang.

Instal library yang dibutuhkan:

`pip install tabulate`

Jalankan program utama:

`python main.py`


## 9. Kesimpulan

Program Sistem Manajemen Keuangan telah mengintegrasikan konsep abstraksi dan polimorfisme untuk memisahkan tanggung jawab antarkelas dan mengurangi ketergantungan terhadap pemeriksaan jenis objek.

Abstraksi diterapkan pada class `Transaksi`, polimorfisme melalui overriding diterapkan pada `Pemasukan` dan `Pengeluaran`, duck typing diterapkan pada class laporan, serta operator overloading diterapkan melalui `Dompet.__str__()`.

Hubungan antarkelas juga dimodelkan menggunakan asosiasi, agregasi, dan komposisi. Selain itu, prinsip Open/Closed Principle diterapkan untuk mendukung pengembangan jenis transaksi baru tanpa mengubah logika utama pencatatan dompet.