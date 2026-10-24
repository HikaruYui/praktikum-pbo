
from tabulate import tabulate


class User:
    aplikasi = "Aplikasi Manajemen Keuangan"
    jumlah_user = 0

    def __init__(self, nama, email):
        if not self.validasi_email(email):
            raise ValueError("Format email tidak valid.")

        self.nama = nama
        self.email = email
        self.__password = ""
        self.daftar_dompet = []
        User.jumlah_user += 1

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, nilai):
        if len(nilai) < 6:
            raise ValueError("Password minimal 6 karakter.")
        self.__password = nilai

    def profile(self):
        print(tabulate(
            [
                ["Nama", self.nama],
                ["Email", self.email]
            ],
            headers=["Data", "Keterangan"],
            tablefmt="grid"
        ))

    def tambah_dompet(self, dompet):
        self.daftar_dompet.append(dompet)

    def lihat_transaksi(self, transaksi):
        transaksi.tampilkan()

    @classmethod
    def total_user(cls):
        return User.jumlah_user

    @staticmethod
    def validasi_email(email):
        return isinstance(email, str) and "@" in email
