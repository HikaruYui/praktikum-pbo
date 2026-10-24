
from tabulate import tabulate
from textwrap import fill
from transaksi import Transaksi
from dompet import Dompet

def bukti_abstraksi():
    print("=== BUKTI PENERAPAN ABSTRAKSI ===")
    print("\n[1] Pengujian Abstract Class")
    try:
        Transaksi("Contoh", 10000, "Umum")
    except TypeError as error:
        data = [
            [
                "Transaksi",
                "TypeError",
                fill(str(error), width=45)
            ]
        ]

        print(tabulate(
            data,
            headers=["Class", "Hasil", "Keterangan"],
            tablefmt="grid"
        ))

    
    # 2. Bukti method konkret digunakan kedua subclass
    print("\n[2] Pengujian Method Konkret")
    dompet = Dompet("Dompet Uji", 100000)
    pemasukan = dompet.tambah_pemasukan(
        "Gaji", 50000, "Kantor"
    )
    pengeluaran = dompet.tambah_pengeluaran(
        "Makan", 25000, "Tunai"
    )

    data = []

    for transaksi in [pemasukan, pengeluaran]:
        data.append([
            transaksi.tipe,
            transaksi.ringkasan()
        ])

    print(tabulate(
        data,
        headers=["Subclass", "Hasil Method Konkret ringkasan()"],
        tablefmt="grid"
    ))

if __name__ == "__main__":
    bukti_abstraksi()
