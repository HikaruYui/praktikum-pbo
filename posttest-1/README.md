# Posttest 1 - Sistem Manajemen Keuangan

Posttest 1 merupakan program sederhana berbasis Python dengan tema **Sistem Manajemen Keuangan**.

Program dibuat menggunakan pendekatan Object-Oriented Programming (OOP) dengan menerapkan materi:

- Class & Object
- Class Attribute
- Instance Attribute
- Public Attribute
- Private Attribute
- Instance Method
- Class Method
- Static Method
- Encapsulation
- Property
- Getter dan Setter
- Validasi Data

Program tidak menggunakan database sehingga seluruh objek dan data hanya digunakan selama program dijalankan.

---

# Struktur File

```text
posttest-1/
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
- `README.md` berisi dokumentasi Posttest 1.

---

# Class yang Digunakan

Program memiliki tiga class utama:

```text
User
Dompet
Transaksi
```

Ketiga class tersebut digunakan untuk merepresentasikan pengguna, dompet, dan transaksi pada Sistem Manajemen Keuangan.

---

## 1. Class User

Class `User` digunakan untuk menyimpan dan mengelola data pengguna.

```python
class User:
```

### Atribut

Class attribute:

```python
aplikasi = "Aplikasi Manajemen Keuangan"
jumlah_user = 0
```

Instance attribute:

```python
self.nama
self.email
self.__password
```

`nama` dan `email` merupakan public attribute, sedangkan:

```python
self.__password
```

merupakan private attribute yang digunakan untuk menyimpan password pengguna.

### Instance Method

Method:

```python
profile()
```

digunakan untuk menampilkan nama dan email pengguna dalam bentuk tabel.

### Class Method

Method:

```python
@classmethod
def total_user(cls):
```

digunakan untuk mengetahui jumlah objek `User` yang telah dibuat.

### Static Method

Method:

```python
@staticmethod
def validasi_email(email):
```

digunakan untuk melakukan validasi sederhana terhadap alamat email.

Email dianggap valid apabila memiliki karakter:

```text
@
```

### Property dan Setter

Atribut private `__password` diakses melalui property:

```python
@property
def password(self):
    return self.__password
```

Perubahan password dilakukan melalui setter:

```python
@password.setter
def password(self, value):
    if len(value) < 6:
        raise ValueError("Password terlalu mudah")

    self.__password = value
```

Password harus memiliki minimal 6 karakter.

---

## 2. Class Dompet

Class `Dompet` digunakan untuk menyimpan informasi dompet dan saldo pengguna.

```python
class Dompet:
```

### Atribut

Class attribute:

```python
total_dompet = 0
mata_uang = "Rupiah"
aplikasi = "Aplikasi Manajemen Keuangan"
```

Instance attribute:

```python
self.nama
self.__saldo
```

`nama` merupakan public attribute, sedangkan:

```python
self.__saldo
```

merupakan private attribute.

### Instance Method

Method:

```python
cek_saldo()
```

digunakan untuk menampilkan nama dompet dan saldo dalam bentuk tabel.

### Class Method

Method:

```python
@classmethod
def jumlah_dompet(cls):
```

digunakan untuk mengetahui jumlah objek `Dompet` yang telah dibuat.

### Static Method

Method:

```python
@staticmethod
def format_uang(nilai):
```

digunakan sebagai fungsi bantuan untuk memberikan format Rupiah.

Contoh:

```python
Dompet.format_uang(500000)
```

menghasilkan:

```text
Rp500000
```

### Property dan Setter

Saldo diakses melalui property:

```python
@property
def saldo(self):
    return self.__saldo
```

Sedangkan perubahan saldo dilakukan melalui:

```python
@saldo.setter
def saldo(self, value):
    if value < 0:
        raise ValueError("Saldo tidak boleh negatif")

    self.__saldo = value
```

Saldo tidak diperbolehkan memiliki nilai negatif.

---

## 3. Class Transaksi

Class `Transaksi` digunakan untuk menyimpan data transaksi keuangan.

```python
class Transaksi:
```

### Atribut

Class attribute:

```python
jumlah_data = 0
nama_aplikasi = "Aplikasi Manajemen Keuangan"
kategori_default = "Umum"
```

Instance attribute:

```python
self.kategori
self.tipe
self.__jumlah
```

`kategori` dan `tipe` merupakan public attribute.

Sedangkan:

```python
self.__jumlah
```

merupakan private attribute yang digunakan untuk menyimpan nominal transaksi.

### Instance Method

Method:

```python
tampilkan()
```

digunakan untuk menampilkan kategori, tipe, dan jumlah transaksi dalam bentuk tabel.

### Class Method

Method:

```python
@classmethod
def total_transaksi(cls):
```

digunakan untuk mengetahui jumlah objek transaksi yang telah dibuat.

### Static Method

Method:

```python
@staticmethod
def cek_tipe(tipe):
```

digunakan untuk mengecek apakah tipe transaksi merupakan:

```text
Pemasukan
```

atau:

```text
Pengeluaran
```

### Property dan Setter

Jumlah transaksi diakses melalui property:

```python
@property
def jumlah(self):
    return self.__jumlah
```

Sedangkan perubahan jumlah transaksi dilakukan melalui setter:

```python
@jumlah.setter
def jumlah(self, nilai):
    if nilai <= 0:
        raise ValueError("Jumlah harus lebih dari 0.")

    self.__jumlah = nilai
```

Jumlah transaksi harus lebih dari `0`.

---

# Konsep OOP yang Diterapkan

## Class dan Object

Program memiliki tiga class:

```text
User
Dompet
Transaksi
```

Pada `main.py`, dibuat dua objek dari setiap class.

Objek User:

```python
u1 = User("Hikaru", "hikaru@gmail.com")
u2 = User("Yui", "yui@gmail.com")
```

Objek Dompet:

```python
d1 = Dompet("Dompet Utama", 500000)
d2 = Dompet("Tabungan", 1000000)
```

Objek Transaksi:

```python
t1 = Transaksi("Makan", 25000, "Pengeluaran")
t2 = Transaksi("Gaji", 3000000, "Pemasukan")
```

---

## Class Attribute

Class attribute merupakan atribut yang dimiliki oleh class dan digunakan bersama oleh seluruh objek.

Contoh pada class `Dompet`:

```python
total_dompet = 0
mata_uang = "Rupiah"
aplikasi = "Aplikasi Manajemen Keuangan"
```

Contoh pada class `Transaksi`:

```python
jumlah_data = 0
nama_aplikasi = "Aplikasi Manajemen Keuangan"
kategori_default = "Umum"
```

---

## Instance Attribute

Instance attribute merupakan atribut yang dimiliki oleh masing-masing objek dan dibuat melalui constructor `__init__()`.

Contoh:

```python
def __init__(self, nama, saldo):
    self.nama = nama
    self.saldo = saldo
```

Nilai instance attribute dapat berbeda pada setiap objek.

---

## Public Attribute

Public attribute dapat diakses secara langsung dari luar class.

Contoh:

```python
self.nama
self.email
self.kategori
self.tipe
```

---

## Private Attribute

Private attribute digunakan untuk membatasi akses langsung terhadap data tertentu.

Program menggunakan:

```python
User.__password
Dompet.__saldo
Transaksi.__jumlah
```

Atribut tersebut tidak diubah secara langsung dari luar class, melainkan melalui property dan setter.

---

# Encapsulation dan Property

Encapsulation diterapkan dengan menggunakan private attribute dan property.

Contohnya pada class `Dompet`:

```python
@property
def saldo(self):
    return self.__saldo
```

Setter digunakan untuk melakukan perubahan sekaligus validasi:

```python
@saldo.setter
def saldo(self, value):
    if value < 0:
        raise ValueError("Saldo tidak boleh negatif")

    self.__saldo = value
```

Konsep yang sama diterapkan pada:

```text
User.password
Dompet.saldo
Transaksi.jumlah
```

---

# Instance Method

Instance method merupakan method yang menggunakan parameter `self` dan bekerja terhadap data objek.

Contoh penggunaannya:

```python
u1.profile()
d1.cek_saldo()
t1.tampilkan()
```

---

# Class Method

Class method menggunakan decorator:

```python
@classmethod
```

dan menerima parameter `cls`.

Program menggunakan:

```python
User.total_user()
Dompet.jumlah_dompet()
Transaksi.total_transaksi()
```

Method tersebut digunakan untuk mengetahui jumlah objek yang telah dibuat.

---

# Static Method

Static method menggunakan decorator:

```python
@staticmethod
```

dan tidak membutuhkan parameter `self` maupun `cls`.

Program menggunakan:

```python
User.validasi_email("hikaru@gmail.com")
Dompet.format_uang(500000)
Transaksi.cek_tipe("Pemasukan")
```

---

# Validasi Data

Program menerapkan validasi menggunakan setter.

## Validasi Password

Password harus memiliki minimal 6 karakter.

Data valid:

```python
u1.password = "password123"
```

Data tidak valid:

```python
u2.password = "123"
```

Program menghasilkan:

```text
Password terlalu mudah
```

---

## Validasi Saldo

Saldo tidak boleh bernilai negatif.

Data valid:

```python
d1.saldo = 750000
```

Data tidak valid:

```python
d2.saldo = -100000
```

Program menghasilkan:

```text
Saldo tidak boleh negatif
```

---

## Validasi Jumlah Transaksi

Jumlah transaksi harus lebih dari `0`.

Data valid:

```python
t1.jumlah = 50000
```

Data tidak valid:

```python
t2.jumlah = 0
```

Program menghasilkan:

```text
Jumlah harus lebih dari 0.
```

Pengujian data tidak valid menggunakan `try-except` agar program tetap dapat menjalankan pengujian berikutnya setelah terjadi `ValueError`.

---

# Pengujian Program

Seluruh pengujian dilakukan pada file:

```text
main.py
```

Pengujian meliputi:

```text
1. Membuat dua objek User
2. Membuat dua objek Dompet
3. Membuat dua objek Transaksi
4. Menjalankan instance method
5. Menjalankan class method
6. Menjalankan static method
7. Menguji setter dengan data valid
8. Menguji setter dengan data tidak valid
```

Contoh pemanggilan instance method:

```python
u1.profile()
d1.cek_saldo()
t1.tampilkan()
```

Pengujian class method:

```python
print("Total user:", User.total_user())
print("Total dompet:", Dompet.jumlah_dompet())
print("Total transaksi:", Transaksi.total_transaksi())
```

Pengujian static method:

```python
User.validasi_email("hikaru@gmail.com")
Dompet.format_uang(500000)
Transaksi.cek_tipe("Pemasukan")
```

---

# Library yang Digunakan

Program menggunakan library:

```text
tabulate
```

Library tersebut digunakan untuk menampilkan informasi dalam bentuk tabel.

Install menggunakan:

```bash
pip install tabulate
```

---

# Cara Menjalankan Program

Masuk ke folder Posttest 1:

```bash
cd posttest-1
```

Install library apabila belum tersedia:

```bash
pip install tabulate
```

Kemudian jalankan:

```bash
python3 -m main
```

atau:

```bash
python3 main.py
```

---

# Kesimpulan

Posttest 1 Sistem Manajemen Keuangan telah menerapkan materi dari tiga modul OOP, yaitu:

```text
Modul 1 : Class & Object
Modul 2 : Atribut & Method
Modul 3 : Encapsulation & Property
```

Program memiliki tiga class utama:

```text
User
Dompet
Transaksi
```

Program juga telah menerapkan:

```text
Class Attribute
Instance Attribute
Public Attribute
Private Attribute
Instance Method
Class Method
Static Method
Property
Getter
Setter
Validasi Data
```

Pada `main.py`, dibuat minimal dua objek dari setiap class serta dilakukan pengujian terhadap instance method, class method, static method, setter dengan data valid, dan setter dengan data tidak valid.
