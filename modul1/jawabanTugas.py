
# Program OOP: Data Mahasiswa STITEK Bontang

# 1. Membuat Class Mahasiswa
class Mahasiswa:

    # Class Attribute
    universitas = "STITEK Bontang"

    # 2. Constructor dan Instance Attributes
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # 3. Method perkenalan diri
    def perkenalan_diri(self):
        return (f"Halo, nama saya {self.nama}, "
                f"NIM {self.nim}, "
                f"jurusan {self.jurusan}, "
                f"IPK {self.ipk}. "
                f"Saya mahasiswa {Mahasiswa.universitas}.")

    # 4. Method untuk update IPK
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}"
        else:
            return "IPK harus berada di antara 0.0 sampai 4.0"

    # 5. Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Memenuhi Syarat Kelulusan"


# 6. Instansiasi 3 Object Mahasiswa

mahasiswa1 = Mahasiswa(
    "Nadiva", "202512014", "Teknik Informatika", 3.9
)

mahasiswa2 = Mahasiswa(
    "Piah", "202512009", "Teknik Informatika", 3.8
)

mahasiswa3 = Mahasiswa(
    "Kia", "202512013", "Teknik Informatika", 3.7
)


# 7. Demonstrasi Method perkenalan_diri()
print("===== DATA MAHASISWA =====")

print(mahasiswa1.perkenalan_diri())
print(mahasiswa2.perkenalan_diri())
print(mahasiswa3.perkenalan_diri())


# 8. Demonstrasi Method update_ipk()
print("\n===== UPDATE IPK =====")

print(mahasiswa1.update_ipk(3.95))


# 9. Demonstrasi Method predikat_kelulusan()
print("\n===== PREDIKAT KELULUSAN =====")

print(f"{mahasiswa1.nama}: {mahasiswa1.predikat_kelulusan()}")
print(f"{mahasiswa2.nama}: {mahasiswa2.predikat_kelulusan()}")
print(f"{mahasiswa3.nama}: {mahasiswa3.predikat_kelulusan()}")


# 10. Menampilkan Class Attribute
print("\n===== INFORMASI UNIVERSITAS =====")
print("Universitas:", Mahasiswa.universitas)
