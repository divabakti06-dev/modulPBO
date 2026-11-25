class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    # Jawaban soal a: method untuk mengembalikan jumlah mahasiswa
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


if __name__ == "__main__":
    # Jawaban soal b: Membuat 2 mata kuliah dan 3 mahasiswa
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Pemrograman Berorientasi Objek")

    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    # Mendaftarkan mahasiswa ke masing-masing mata kuliah
    mk1.tambah_mahasiswa(m1)
    mk1.tambah_mahasiswa(m2)

    mk2.tambah_mahasiswa(m1)
    mk2.tambah_mahasiswa(m2)
    mk2.tambah_mahasiswa(m3)

    # Jawaban soal c: Menampilkan daftar mahasiswa dan jumlah mahasiswanya
    print(f"Mata Kuliah      : {mk1.nama} ({mk1.kode})")
    print(f"Daftar Mahasiswa : {mk1.daftar_mahasiswa()}")
    print(f"Jumlah Mahasiswa : {mk1.jumlah_mahasiswa()}")

    print("-" * 45)

    print(f"Mata Kuliah      : {mk2.nama} ({mk2.kode})")
    print(f"Daftar Mahasiswa : {mk2.daftar_mahasiswa()}")
    print(f"Jumlah Mahasiswa : {mk2.jumlah_mahasiswa()}")