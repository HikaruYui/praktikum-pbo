from tabulate import tabulate
from transaksi import Transaksi, Pemasukan, Pengeluaran


class Dompet:
    total_dompet = 0
    mata_uang = "Rupiah"
    aplikasi = "Aplikasi Manajemen Keuangan"

    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
        self.__daftar_transaksi = []
        Dompet.total_dompet += 1

    @property
    def saldo(self):
        return self.__saldo  

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            raise ValueError("Saldo tidak boleh negatif.")
        self.__saldo = nilai

    @property
    def daftar_transaksi(self):
        return tuple(self.__daftar_transaksi)

    def cek_saldo(self):
        print(tabulate(
            [["Nama Dompet", self.nama],
             ["Saldo", self.format_uang(self.saldo)]],
            headers=["Data", "Keterangan"],
            tablefmt="grid",
        ))

    #Ini solid ya, masuknya open closed
    def tambah_transaksi(self, kelas_transaksi, kategori, jumlah, detail):
        transaksi = kelas_transaksi(kategori, jumlah, detail)
        saldo_baru = self.saldo + transaksi.perubahan_saldo()

        if saldo_baru < 0:  
            raise ValueError("Saldo Anda tidak mencukupi.")

        self.saldo = saldo_baru
        transaksi._daftarkan()
        self.__daftar_transaksi.append(transaksi)
        return transaksi

    def tambah_pemasukan(self, kategori, jumlah, sumber):
        return self.tambah_transaksi(Pemasukan, kategori, jumlah, sumber)

    def tambah_pengeluaran(self, kategori, jumlah, metode_pembayaran):
        return self.tambah_transaksi(
            Pengeluaran, kategori, jumlah, metode_pembayaran
        )

    #overloading
    def __str__(self):
        return f"Dompet '{self.nama}' (saldo: {self.format_uang(self.saldo)})"

    @classmethod
    def jumlah_dompet(cls):
        return Dompet.total_dompet

    @staticmethod
    def format_uang(nilai):
        return f"Rp{nilai:,.0f}"
