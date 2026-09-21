from user import User
from dompet import Dompet
from transaksi import Transaksi

# 2 object User
u1 = User("Hikaru", "hikaru@gmail.com")
u2 = User("Yui", "yui@gmail.com")

# 2 object Dompet
d1 = Dompet("Dompet Utama", 500000)
d2 = Dompet("Tabungan", 1000000)

# 2 object Transaksi
t1 = Transaksi("Makan", 25000, "Pengeluaran")
t2 = Transaksi("Gaji", 3000000, "Pemasukan")

u1.profile()
d1.cek_saldo()
t1.tampilkan()

print("Total user:", User.total_user())
print("Total dompet:", Dompet.jumlah_dompet())
print("Total transaksi:", Transaksi.total_transaksi())

print(
    "Email valid:",
    User.validasi_email("hikaru@gmail.com")
)

print(
    "Format uang:",
    Dompet.format_uang(500000)
)

print(
    "Tipe transaksi valid:",
    Transaksi.cek_tipe("Pemasukan")
)

u1.password = "password123"
print("Password berhasil diubah")

d1.saldo = 750000
print("Saldo berhasil diubah menjadi:", d1.saldo)

t1.jumlah = 50000
print("Jumlah transaksi berhasil diubah menjadi:", t1.jumlah)

# Password kurang dari 6 karakter
try:
    u2.password = "123"
except ValueError as e:
    print("User:", e)


# Saldo negatif
try:
    d2.saldo = -100000
except ValueError as e:
    print("Dompet:", e)


# Jumlah transaksi 0
try:
    t2.jumlah = 0
except ValueError as e:
    print("Transaksi:", e)