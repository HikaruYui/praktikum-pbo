from abc import ABC, abstractmethod
from tabulate import tabulate


class Transaksi(ABC):
    jumlah_data = 0
    nama_aplikasi = "Aplikasi Manajemen Keuangan"

    def __init__(self, kategori, jumlah, tipe):
        self.kategori = kategori
        self.tipe = tipe
        self.jumlah = jumlah
        self.__id_transaksi = None

    @property
    def jumlah(self):
        return self._jumlah  

    @jumlah.setter
    def jumlah(self, nilai):
        if nilai <= 0:
            raise ValueError("Jumlah transaksi harus lebih dari 0.")
        self._jumlah = nilai

    def _daftarkan(self):
        if self.__id_transaksi is None:
            Transaksi.jumlah_data += 1
            self.__id_transaksi = f"{Transaksi.jumlah_data:03d}"

    def get_id_transaksi(self):
        return self.__id_transaksi or "Belum dicatat"

    def ringkasan(self):
        return (
            f"{self.get_id_transaksi()} | {self.tipe}: {self.kategori} | "
            f"perubahan saldo {self.perubahan_saldo():+,.0f}"
        )

    @abstractmethod
    def perubahan_saldo(self):
        """Kembalikan perubahan saldo bertanda (+ pemasukan, - pengeluaran)."""

    @abstractmethod
    def tampilkan(self):
        """Tampilkan informasi spesifik jenis transaksi."""

    @classmethod
    def total_transaksi(cls):
        return Transaksi.jumlah_data


class Pemasukan(Transaksi):
    def __init__(self, kategori, jumlah, sumber):
        super().__init__(kategori, jumlah, "Pemasukan")
        self.sumber = sumber 

    def perubahan_saldo(self):
        return self._jumlah

    def tampilkan(self):
        print(tabulate(
            [[self.get_id_transaksi(), self.kategori, self.tipe,
              f"Rp{self._jumlah:,.0f}", self.sumber]],
            headers=["ID", "Kategori", "Jenis", "Jumlah", "Sumber"],
            tablefmt="grid",
        ))


class Pengeluaran(Transaksi):
    def __init__(self, kategori, jumlah, metode_pembayaran):
        super().__init__(kategori, jumlah, "Pengeluaran")
        self.metode_pembayaran = metode_pembayaran  

    def perubahan_saldo(self):
        return -self._jumlah

    def tampilkan(self):
        print(tabulate(
            [[self.get_id_transaksi(), self.kategori, self.tipe,
              f"Rp{self._jumlah:,.0f}", self.metode_pembayaran]],
            headers=["ID", "Kategori", "Jenis", "Jumlah", "Metode Bayar"],
            tablefmt="grid",
        ))
