from user import User
from dompet import Dompet
from transaksi import Transaksi

u1 = User("Hikaru", "hikaru@gmail.com")
u2 = User("Yui", "yui@gmail.com")

d1 = Dompet("Dompet Utama", 500000)
d2 = Dompet("Tabungan", 1000000)

u1.tambah_dompet(d1)
u2.tambah_dompet(d2)


t1 = d1.tambah_pengeluaran(
    "Makan",
    25000,
    "QRIS"
)

t2 = d1.tambah_pemasukan(
    "Gaji",
    3000000,
    "Kantor"
)


u1.profile()
print()

d1.cek_saldo()
print()

u1.lihat_transaksi(t1)
print()

u1.lihat_transaksi(t2)
print("\nTotal user:", User.total_user())
print("Total dompet:", Dompet.jumlah_dompet())
print("Total transaksi:", Transaksi.total_transaksi())