
# a. Class ManajerInventori
class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    # b. Method untuk menambahkan barang
    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah

            return f"Berhasil menambahkan {jumlah} {nama_barang}"

        return "Jumlah barang harus positif"

    # b. Method untuk mengurangi stok barang
    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori and 0 < jumlah <= self.inventori[nama_barang]:
            self.inventori[nama_barang] -= jumlah

            if self.inventori[nama_barang] == 0:
                del self.inventori[nama_barang]

            return f"Berhasil mengurangi {jumlah} {nama_barang}"

        return "Barang tidak tersedia atau stok tidak mencukupi"

    # a. Method untuk melihat inventori
    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori masih kosong"

        return f"Daftar Inventori: {self.inventori}"


# c. Testing atau pengujian program

# Membuat object
inventori = ManajerInventori()

# Menambahkan barang
print(inventori.tambah_barang("Laptop", 10))
print(inventori.tambah_barang("Mouse", 20))

# Mengurangi stok barang
print(inventori.hapus_barang("Laptop", 2))

# Melihat inventori
print(inventori.lihat_inventori())
