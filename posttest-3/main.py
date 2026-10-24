from dompet import Dompet
from laporan import LaporanRiwayat, LaporanSaldo, cetak_laporan
from transaksi import Transaksi
from user import User
from tabulate import tabulate

def main():
    print("=== SISTEM MANAJEMEN KEUANGAN===")
    u1 = User("Hikaru", "hikaru@gmail.com")
    u2 = User("Yui", "yui@gmail.com")

    d1 = Dompet("Dompet Utama", 500000)
    d2 = Dompet("Tabungan", 1000000)

    u1.tambah_dompet(d1)
    u2.tambah_dompet(d2)

    # Agregasi
    u1.tambah_dompet(d1)
    u2.tambah_dompet(d2)

    # Membuat transaksi
    t1 = d1.tambah_pengeluaran("Makan", 25000, "QRIS")
    t2 = d1.tambah_pemasukan("Gaji", 3000000, "Kantor")

    # 1. Menampilkan profil dan saldo
    
    print("\n[1] Enkapsulasi dan agregasi: Profil & Saldo")

    data = [
        ["Nama", u1.nama],
        ["Email", u1.email],
        ["Nama Dompet", d1.nama],
        ["Saldo", d1.format_uang(d1.saldo)]
    ]

    print(tabulate(
        data,
        headers=["Data", "Keterangan"],
        tablefmt="grid"
    ))
    
    print("\n[2] Polimorfisme via inheritance dan komposisi: Riwayat Transaksi")
    data = []
    for transaksi in d1.daftar_transaksi:
        data.append([
            transaksi.get_id_transaksi(),
            transaksi.kategori,
            transaksi.tipe,
            d1.format_uang(transaksi.jumlah),
            f"{transaksi.perubahan_saldo():+,.0f}"
        ])
    print(tabulate(
        data,
        headers=[
            "ID",
            "Kategori",
            "Jenis",
            "Jumlah",
            "Perubahan (Rp)"
        ],
        tablefmt="grid"
    ))

    # 3. Asosiasi
    print("\n[3] Dependency (asosiasi objek): User memakai objek Transaksi")
    u1.lihat_transaksi(t1)

    # 4. Duck Typing
    print("\n[4] Laporan Keuangan (Duck Typing)")

    for laporan in [LaporanSaldo(d1), LaporanRiwayat(d1)]:
        cetak_laporan(laporan)

    # 6. Bukti abstract class
    try:
        Transaksi("Contoh", 10000, "Transaksi dasar")
    except TypeError as error:
        print(f"TypeError (sesuai harapan): {error}")

    # 7. Validasi saldo
    try:
        d2.tambah_pengeluaran("Laptop", 2000000, "Transfer")
    except ValueError as error:
        print(f"ValueError: {error}")

    # 8. Total objek
    print("\n[8] Total objek tercatat")
    print("Total user:", User.total_user())
    print("Total dompet:", Dompet.jumlah_dompet())
    print("Total transaksi:", Transaksi.total_transaksi())


if __name__ == "__main__":
    main()


