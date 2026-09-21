from tabulate import tabulate


class Transaksi:
    jumlah_data = 0
    nama_aplikasi = "Aplikasi Manajemen Keuangan"
    kategori_default = "Umum"

    def __init__(self, kategori, jumlah, tipe):
        self.kategori = kategori
        self.tipe = tipe
        self.jumlah = jumlah

        Transaksi.jumlah_data += 1

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if nilai <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        self.__jumlah = nilai

    def tampilkan(self):
        data = [
            [self.kategori, self.tipe, f"Rp{self.__jumlah:,.0f}"]
        ]

        print(tabulate(
            data,
            headers=["Kategori", "Tipe", "Jumlah"],
            tablefmt="grid"
        ))

    @classmethod
    def total_transaksi(cls):
        return cls.jumlah_data

    @staticmethod
    def cek_tipe(tipe):
        return tipe.lower() in [
            "pemasukan",
            "pengeluaran"
        ]