
# a. Class Dosen dengan atribut nama dan nidn

class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    # b. Method ajar_mata_kuliah()
    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} mengajar mata kuliah {mata_kuliah}"


# c. Pembuatan 2 object dosen
dosen1 = Dosen("Pak Ahmad", "123456")
dosen2 = Dosen("Bu Siti", "789012")

# Memanggil method
print(dosen1.ajar_mata_kuliah("Pemrograman Python"))
print(dosen2.ajar_mata_kuliah("Basis Data"))
