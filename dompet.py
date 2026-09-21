from tabulate import tabulate


class Dompet:
    total_dompet = 0
    mata_uang = "Rupiah"
    aplikasi = "Aplikasi Manajemen Keuangan"

    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

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

    @classmethod
    def jumlah_dompet(cls):
        return cls.total_dompet

    @staticmethod
    def format_uang(nilai):
        return f"Rp{nilai}"