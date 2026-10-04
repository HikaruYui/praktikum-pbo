from tabulate import tabulate
from transaksi import Pemasukan, Pengeluaran

class Dompet:
    total_dompet = 0
    mata_uang = "Rupiah"
    aplikasi = "Aplikasi Manajemen Keuangan"

    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
        self.daftar_transaksi = []
        Dompet.total_dompet += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if value < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.__saldo = value

    def cek_saldo(self):
        data = [
            ["Nama Dompet", self.nama],
            ["Saldo", self.format_uang(self.__saldo)]
        ]

        print(tabulate(
            data,
            headers=["Data", "Keterangan"],
            tablefmt="grid"
        ))

    def tambah_pemasukan(self, kategori, jumlah, sumber):
        transaksi = Pemasukan(kategori, jumlah, sumber)

        self.daftar_transaksi.append(transaksi)
        self.saldo += jumlah
        
        return transaksi

    def tambah_pengeluaran(self, kategori, jumlah, metode_pembayaran):
        if jumlah > self.saldo:
            print("Saldo Anda tidak mencukupi.")
            return
        
        transaksi = Pengeluaran(
            kategori,
            jumlah,
            metode_pembayaran
        )

        self.daftar_transaksi.append(transaksi)
        self.saldo -= jumlah
        return transaksi

    @classmethod
    def jumlah_dompet(cls):
        return cls.total_dompet

    @staticmethod
    def format_uang(nilai):
        return f"Rp{nilai}"