class Mahasiswa:
    def __init__(self, nama: str, nim: str, ipk = 0):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk
    def show(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, IPK: {self.ipk}")

mahasiswa1 = Mahasiswa('Joko', 20242025, 4.0)
mahasiswa2 = Mahasiswa('Anton', 20242026)

mahasiswa1.show()
mahasiswa2.show()