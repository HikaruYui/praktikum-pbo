from tabulate import tabulate


class User:
    aplikasi = "Aplikasi Manajemen Keuangan"
    jumlah_user = 0

    def __init__(self, nama, email):
        if not self.validasi_email(email):
            raise ValueError("Format email tidak valid")

        self.nama = nama
        self.email = email
        self.__password = ""

        User.jumlah_user += 1

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Password terlalu mudah")

        self.__password = value

    def profile(self):
        data = [
            ["Nama", self.nama],
            ["Email", self.email]
        ]

        print(tabulate(
            data,
            headers=["Data", "Keterangan"],
            tablefmt="grid"
        ))

    @classmethod
    def total_user(cls):
        return cls.jumlah_user

    @staticmethod
    def validasi_email(email):
        return "@" in email