
# a. Class Kendaraan dengan class attribute
class Kendaraan:
    bahan_bakar = "Bensin"

    # b. Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun


# Membuat object
kendaraan1 = Kendaraan("Toyota", "Hitam", 2023)
kendaraan2 = Kendaraan("Honda", "Merah", 2022)

# c. Mengakses instance attribute
print("Kendaraan 1:")
print(f"Merk: {kendaraan1.merk}")
print(f"Warna: {kendaraan1.warna}")
print(f"Tahun: {kendaraan1.tahun}")

print("\nKendaraan 2:")
print(f"Merk: {kendaraan2.merk}")
print(f"Warna: {kendaraan2.warna}")
print(f"Tahun: {kendaraan2.tahun}")

# Mengakses class attribute
print(f"\nBahan bakar: {Kendaraan.bahan_bakar}")
