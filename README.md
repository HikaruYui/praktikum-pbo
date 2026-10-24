# Sistem Manajemen Keuangan 

Program ini merupakan aplikasi sederhana berbasis Python untuk mengelola data pengguna, dompet, dan transaksi keuangan pribadi. Program dibuat menggunakan pendekatan Object-Oriented Programming (OOP) dan menerapkan materi Class & Object, Atribut & Method, serta Encapsulation & Property.

Program ini tidak menggunakan database sehingga seluruh objek dan data digunakan selama program dijalankan.

## Fitur Program

Program memiliki beberapa fitur utama:

- Menyimpan data pengguna.
- Menampilkan profil pengguna.
- Menyimpan data dompet dan saldo.
- Menampilkan saldo dompet.
- Mencatat transaksi pemasukan dan pengeluaran.
- Menampilkan informasi transaksi.
- Melakukan validasi email.
- Melakukan validasi password.
- Melakukan validasi saldo.
- Melakukan validasi jumlah transaksi.

## Struktur Program

Program terdiri dari tiga class utama:

### 1. Class User

Class `User` digunakan untuk menyimpan dan mengelola data pengguna.

Atribut yang digunakan:

- `aplikasi` sebagai atribut class.
- `jumlah_user` sebagai atribut class.
- `nama` sebagai atribut public.
- `email` sebagai atribut public.
- `__password` sebagai atribut private.

Method yang digunakan:

- `profile()` sebagai instance method untuk menampilkan profil pengguna.
- `total_user()` sebagai class method untuk mengetahui jumlah objek User.
- `validasi_email()` sebagai static method untuk melakukan validasi email.
- `password` sebagai property untuk mengakses atribut private `__password`.
- `password.setter` untuk mengubah password dengan validasi minimal 6 karakter.

### 2. Class Dompet

Class `Dompet` digunakan untuk menyimpan dan mengelola data dompet pengguna.

Atribut yang digunakan:

- `total_dompet` sebagai atribut class.
- `mata_uang` sebagai atribut class.
- `aplikasi` sebagai atribut class.
- `nama` sebagai atribut public.
- `__saldo` sebagai atribut private.

Method yang digunakan:

- `cek_saldo()` sebagai instance method untuk menampilkan informasi saldo.
- `jumlah_dompet()` sebagai class method untuk mengetahui jumlah objek Dompet.
- `format_uang()` sebagai static method untuk memberikan format mata uang.
- `saldo` sebagai property untuk mengakses atribut private `__saldo`.
- `saldo.setter` untuk mengubah saldo dan memastikan saldo tidak bernilai negatif.

### 3. Class Transaksi

Class `Transaksi` digunakan untuk menyimpan data transaksi keuangan.

Atribut yang digunakan:

- `jumlah_data` sebagai atribut class.
- `nama_aplikasi` sebagai atribut class.
- `kategori_default` sebagai atribut class.
- `kategori` sebagai atribut public.
- `tipe` sebagai atribut public.
- `__jumlah` sebagai atribut private.

Method yang digunakan:

- `tampilkan()` sebagai instance method untuk menampilkan informasi transaksi.
- `total_transaksi()` sebagai class method untuk mengetahui jumlah transaksi.
- `cek_tipe()` sebagai static method untuk mengecek tipe transaksi.
- `jumlah` sebagai property untuk mengakses atribut private `__jumlah`.
- `jumlah.setter` untuk mengubah jumlah transaksi dan memastikan nilainya lebih dari 0.

## Konsep OOP yang Digunakan

### Class dan Object

Program menggunakan tiga class utama yaitu:

```text
User
Dompet
Transaksi
```

Pada `main.py` dibuat minimal dua objek dari setiap class untuk melakukan pengujian program.

### Class Attribute

Class attribute merupakan atribut yang dimiliki oleh class dan digunakan bersama oleh seluruh objek.

Contoh:

```python
class Dompet:
    total_dompet = 0
    mata_uang = "Rupiah"
    aplikasi = "Aplikasi Manajemen Keuangan"
```

### Instance Attribute

Instance attribute merupakan atribut yang dimiliki masing-masing objek dan dibuat melalui method `__init__()`.

Contoh:

```python
def __init__(self, nama, saldo):
    self.nama = nama
    self.saldo = saldo
```

### Public Attribute

Public attribute dapat diakses secara langsung dari luar class.

Contoh:

```python
self.nama
self.email
self.kategori
self.tipe
```

### Private Attribute

Private attribute digunakan untuk melindungi data tertentu agar tidak diakses atau diubah secara langsung dari luar class.

Program menggunakan beberapa private attribute:

```python
__password
__saldo
__jumlah
```

### Property, Getter, dan Setter

Atribut private diakses menggunakan decorator `@property` dan diubah menggunakan setter.

Contoh:

```python
@property
def saldo(self):
    return self.__saldo

@saldo.setter
def saldo(self, value):
    if value < 0:
        raise ValueError("Saldo tidak boleh negatif")

    self.__saldo = value
```

Setter juga digunakan untuk melakukan validasi sebelum nilai atribut private diperbarui.

### Instance Method

Instance method merupakan method yang menggunakan parameter `self` dan bekerja terhadap data suatu objek.

Contoh:

```python
user.profile()
dompet.cek_saldo()
transaksi.tampilkan()
```

### Class Method

Class method menggunakan decorator `@classmethod` dan parameter `cls`.

Contoh:

```python
User.total_user()
Dompet.jumlah_dompet()
Transaksi.total_transaksi()
```

### Static Method

Static method merupakan method bantuan yang tidak membutuhkan parameter `self` maupun `cls`.

Contoh:

```python
User.validasi_email("hikaru@gmail.com")
Dompet.format_uang(500000)
Transaksi.cek_tipe("Pemasukan")
```

## Struktur File

```text
praktikum-pbo/
│
├── main.py
├── user.py
├── dompet.py
├── transaksi.py
└── README.md
```

Keterangan:

- `main.py` digunakan untuk menjalankan dan menguji program.
- `user.py` berisi class `User`.
- `dompet.py` berisi class `Dompet`.
- `transaksi.py` berisi class `Transaksi`.
- `README.md` berisi dokumentasi program.

## Library yang Digunakan

Program menggunakan library `tabulate` untuk menampilkan data dalam bentuk tabel agar lebih mudah dibaca.

Install library dengan perintah:

```bash
pip install tabulate
```

## Cara Menjalankan Program

Pastikan Python dan library `tabulate` sudah terinstall.

Clone repository:

```bash
git clone https://github.com/HikaruYui/praktikum-pbo.git
```

Masuk ke folder project:

```bash
cd praktikum-pbo
```

Jalankan program:

```bash
python3 main.py
```

## Pengujian Program

Pengujian dilakukan pada file `main.py`.

### 1. Pengujian Object

Program membuat minimal dua objek dari setiap class:

```python
u1 = User("Hikaru", "hikaru@gmail.com")
u2 = User("Yui", "yui@gmail.com")

d1 = Dompet("Dompet Utama", 500000)
d2 = Dompet("Tabungan", 1000000)

t1 = Transaksi("Makan", 25000, "Pengeluaran")
t2 = Transaksi("Gaji", 3000000, "Pemasukan")
```

### 2. Pengujian Instance Method

```python
u1.profile()
d1.cek_saldo()
t1.tampilkan()
```

### 3. Pengujian Class Method

```python
User.total_user()
Dompet.jumlah_dompet()
Transaksi.total_transaksi()
```

### 4. Pengujian Static Method

```python
User.validasi_email("hikaru@gmail.com")
Dompet.format_uang(500000)
Transaksi.cek_tipe("Pemasukan")
```

### 5. Pengujian Setter dengan Data Valid

```python
u1.password = "password123"
d1.saldo = 750000
t1.jumlah = 50000
```

Data tersebut dapat diterima karena memenuhi aturan validasi masing-masing setter.

### 6. Pengujian Setter dengan Data Tidak Valid

Password kurang dari 6 karakter:

```python
u2.password = "123"
```

Program akan menolak perubahan password.

Saldo negatif:

```python
d2.saldo = -100000
```

Program akan menghasilkan pesan:

```text
Saldo tidak boleh negatif
```

Jumlah transaksi tidak lebih dari 0:

```python
t2.jumlah = 0
```

Program akan menghasilkan pesan:

```text
Jumlah harus lebih dari 0.
```

Pengujian data tidak valid menggunakan `try-except` agar program tetap dapat menjalankan pengujian berikutnya setelah `ValueError` terjadi.

- Validasi Data

Program juga melakukan pengujian menggunakan minimal dua objek untuk setiap class serta menguji setter menggunakan data valid dan tidak valid.
