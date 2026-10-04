from tabulate import tabulate

class Transaksi:
    jumlah_data = 0
    nama_aplikasi = "Aplikasi Manajemen Keuangan"
    kategori_default = "Umum"

    def __init__(self, kategori, jumlah, tipe):
        Transaksi.jumlah_data += 1

        self.kategori = kategori
        self.tipe = tipe
        self.jumlah = jumlah
        self.__id_transaksi = f"Transaksi{Transaksi.jumlah_data}"

    @property
    def jumlah(self):
        return self._jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if nilai <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        self._jumlah = nilai

    def get_id_transaksi(self):
        return self.__id_transaksi

    def tampilkan(self):
        data = [
            [
                self.__id_transaksi,
                self.kategori,
                self.tipe,
                self._jumlah
            ]
        ]

        print(tabulate(
            data,
            headers=["ID Transaksi", "Kategori", "Tipe", "Jumlah"],
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


class Pemasukan(Transaksi):
    def __init__(self, kategori, jumlah, sumber):
        super().__init__(kategori, jumlah, "Pemasukan")
        self.sumber = sumber


class Pengeluaran(Transaksi):
    def __init__(self, kategori, jumlah, metode_pembayaran):
        super().__init__(kategori, jumlah, "Pengeluaran")
        self.metode_pembayaran = metode_pembayaran

    def tampilkan(self):
        data = [
            [
                self.get_id_transaksi(),
                self.kategori,
                self.tipe,
                self._jumlah,
                self.metode_pembayaran
            ]
        ]

        print(tabulate(
            data,
            headers=[
                "ID Transaksi",
                "Kategori",
                "Tipe",
                "Jumlah",
                "Metode Pembayaran"
            ],
            tablefmt="grid"
        ))