# Posttest 2 - Sistem Manajemen Keuangan

Posttest 2 merupakan pengembangan dari program Sistem Manajemen Keuangan dengan menerapkan materi:

- Relasi UML
  - Asosiasi
  - Agregasi
  - Komposisi
- Inheritance
- Superclass dan Subclass
- `super()`
- Method Overriding
- Protected Attribute
- Private Attribute

Program dibuat menggunakan Python dengan pendekatan Object-Oriented Programming.

---

## Struktur File

```text
posttest-2/
├── main.py
├── user.py
├── dompet.py
├── transaksi.py
└── README.md
```

Keterangan:

- `main.py` digunakan untuk menjalankan program.
- `user.py` berisi class `User`.
- `dompet.py` berisi class `Dompet`.
- `transaksi.py` berisi class `Transaksi`, `Pemasukan`, dan `Pengeluaran`.

---

# Relasi UML

## 1. Asosiasi

Asosiasi diterapkan antara `User` dan `Transaksi`.

```text
User ------> Transaksi
```

Implementasi:

```python
def lihat_transaksi(self, transaksi):
    transaksi.tampilkan()
```

Objek transaksi diterima sebagai parameter oleh method `lihat_transaksi()`.

Contoh:

```python
u1.lihat_transaksi(t1)
```

---

## 2. Agregasi

Agregasi diterapkan antara `User` dan `Dompet`.

```text
User ◇------ Dompet
```

Objek `Dompet` dibuat terlebih dahulu:

```python
d1 = Dompet("Dompet Utama", 500000)
```

Kemudian ditambahkan ke objek `User`:

```python
u1.tambah_dompet(d1)
```

Pada class `User`, objek Dompet disimpan dalam:

```python
self.daftar_dompet = []
```

---

## 3. Komposisi

Komposisi diterapkan antara `Dompet` dan `Transaksi`.

```text
Dompet ◆------ Transaksi
```

Objek transaksi dibuat melalui method milik `Dompet`.

Contoh pemasukan:

```python
transaksi = Pemasukan(kategori, jumlah, sumber)
```

Contoh pengeluaran:

```python
transaksi = Pengeluaran(
    kategori,
    jumlah,
    metode_pembayaran
)
```

Transaksi kemudian disimpan pada:

```python
self.daftar_transaksi
```

---

# Inheritance

Inheritance diterapkan pada class `Transaksi`, `Pemasukan`, dan `Pengeluaran`.

```text
              Transaksi
             /         \
            /           \
      Pemasukan       Pengeluaran
```

`Transaksi` merupakan superclass.

```python
class Transaksi:
```

Sedangkan `Pemasukan` dan `Pengeluaran` merupakan subclass.

```python
class Pemasukan(Transaksi):
```

```python
class Pengeluaran(Transaksi):
```

---

## Penggunaan super()

Kedua subclass memanggil constructor superclass menggunakan `super()`.

### Pemasukan

```python
super().__init__(kategori, jumlah, "Pemasukan")
```

### Pengeluaran

```python
super().__init__(kategori, jumlah, "Pengeluaran")
```

Dengan penggunaan `super()`, atribut dasar transaksi tidak perlu ditulis ulang pada masing-masing subclass.

---

## Atribut Tambahan Subclass

Setiap subclass memiliki atribut khusus.

### Pemasukan

```python
self.sumber = sumber
```

Atribut `sumber` digunakan untuk menyimpan asal pemasukan.

### Pengeluaran

```python
self.metode_pembayaran = metode_pembayaran
```

Atribut `metode_pembayaran` digunakan untuk menyimpan metode pembayaran seperti QRIS atau tunai.

---

## Method Overriding

Method overriding diterapkan pada class `Pengeluaran`.

Superclass `Transaksi` memiliki method:

```python
def tampilkan(self):
```

Class `Pengeluaran` mendefinisikan kembali method tersebut:

```python
def tampilkan(self):
```

Pada `Pengeluaran`, method `tampilkan()` menampilkan informasi tambahan berupa metode pembayaran.

---

# Protected dan Private Attribute

## Protected

Superclass `Transaksi` menggunakan protected attribute:

```python
self._jumlah
```

Atribut `_jumlah` dapat digunakan oleh subclass.

Contohnya pada class `Pengeluaran`:

```python
self._jumlah
```

---

## Private

Superclass `Transaksi` menggunakan private attribute:

```python
self.__id_transaksi
```

Nilai ID transaksi diakses melalui method:

```python
def get_id_transaksi(self):
    return self.__id_transaksi
```

---

# Alur Program

Pada `main.py`, program membuat dua User:

```python
u1 = User("Hikaru", "hikaru@gmail.com")
u2 = User("Yui", "yui@gmail.com")
```

Kemudian membuat dua Dompet:

```python
d1 = Dompet("Dompet Utama", 500000)
d2 = Dompet("Tabungan", 1000000)
```

Dompet ditambahkan kepada User:

```python
u1.tambah_dompet(d1)
u2.tambah_dompet(d2)
```

Kemudian dibuat transaksi pengeluaran:

```python
t1 = d1.tambah_pengeluaran(
    "Makan",
    25000,
    "QRIS"
)
```

dan transaksi pemasukan:

```python
t2 = d1.tambah_pemasukan(
    "Gaji",
    3000000,
    "Kantor"
)
```

Transaksi kemudian dapat dilihat melalui User:

```python
u1.lihat_transaksi(t1)
u1.lihat_transaksi(t2)
```

---

# Library

Program menggunakan library `tabulate` untuk menampilkan data dalam bentuk tabel.

Install dengan:

```bash
pip install tabulate
```

---

# Cara Menjalankan

Masuk ke folder:

```bash
cd posttest-2
```

Jalankan program:

```bash
python3 -m main
```

atau:

```bash
python3 main.py
```

---

# Output Program

Program akan menampilkan:

- Profil User
- Saldo Dompet
- Transaksi Pengeluaran
- Transaksi Pemasukan
- Total User
- Total Dompet
- Total Transaksi

Contoh hasil akhir:

```text
Total user: 2
Total dompet: 2
Total transaksi: 2
```

---

# Kesimpulan

Posttest 2 berhasil menerapkan:

```text
Asosiasi   : User ------> Transaksi
Agregasi   : User ◇------ Dompet
Komposisi  : Dompet ◆---- Transaksi
```

serta inheritance:

```text
              Transaksi
             /         \
      Pemasukan       Pengeluaran
```

Program juga menggunakan:

- `super().__init__()`
- atribut tambahan pada setiap subclass
- method overriding
- protected attribute `_jumlah`
- private attribute `__id_transaksi`
