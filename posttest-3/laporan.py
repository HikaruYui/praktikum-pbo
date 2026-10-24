
from tabulate import tabulate


class LaporanSaldo:
    def __init__(self, dompet):
        self.dompet = dompet

    def cetak(self):
        data = [
            ["Nama Dompet", self.dompet.nama],
            ["Saldo", self.dompet.format_uang(self.dompet.saldo)]
        ]

        print("\nLaporan Saldo:")
        print(tabulate(
            data,
            headers=["Data", "Keterangan"],
            tablefmt="grid"
        ))


class LaporanRiwayat:
    def __init__(self, dompet):
        self.dompet = dompet

    def cetak(self):
        data = []

        for transaksi in self.dompet.daftar_transaksi:
            data.append([
                transaksi.get_id_transaksi(),
                transaksi.kategori,
                transaksi.tipe,
                self.dompet.format_uang(transaksi.jumlah),
                f"{transaksi.perubahan_saldo():+,.0f}"
            ])

        print("\nLaporan Riwayat Transaksi:")
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


def cetak_laporan(laporan):
    laporan.cetak()
