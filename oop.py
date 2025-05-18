class Mahasiswa:
    def __init__(self, nama = 0, nim = 0, alamat = 0):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
    def show(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Alamat: {self.alamat}")

mahasiswa1 = Mahasiswa('Joko', '20242025')
mahasiswa1.show()