class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok
        self.__lokasi_rak = lokasi_rak

    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    def tambah_stok(self, jumlah=1):
        self._stok += jumlah

    def kurangi_stok(self, jumlah=1):
        if self._stok >= jumlah:
            self._stok -= jumlah
            return True
        return False


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []

    def tambah_buku(self, judul, penulis, kode_buku, stok, lokasi_rak):
        buku = Buku(judul, penulis, kode_buku, stok, lokasi_rak)
        self.koleksi_buku.append(buku)
        return buku


class Peminjaman:
    def __init__(self, buku, tanggal_pinjam, tanggal_kembali="-", status="Dipinjam"):
        self.buku = buku
        self.kode_buku = buku.kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return f"{self.buku.judul} ({self.kode_buku}) | Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"


class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3, status_aktif=True):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam
        self.__status_aktif = status_aktif
        self.daftar_peminjaman = []

    def get_status(self):
        return self.__status_aktif

    def set_status(self, status_baru):
        self.__status_aktif = status_baru

    def pinjam_buku(self, buku, tgl_pinjam):
        dipinjam = [p for p in self.daftar_peminjaman if p.status == "Dipinjam"]
        if not self.__status_aktif or len(dipinjam) >= self._maks_pinjam:
            print(f"{self.nama} tidak bisa meminjam.")
            return
        if buku.kurangi_stok():
            self.daftar_peminjaman.append(Peminjaman(buku, tgl_pinjam))
            print(f"{self.nama} meminjam '{buku.judul}'.")
        else:
            print(f"Stok '{buku.judul}' habis.")

    def kembalikan_buku(self, buku, tgl_kembali):
        for p in self.daftar_peminjaman:
            if p.kode_buku == buku.kode_buku and p.status == "Dipinjam":
                p.status = "Dikembalikan"
                p.tanggal_kembali = tgl_kembali
                buku.tambah_stok()
                print(f"{self.nama} mengembalikan '{buku.judul}'.")
                return


if __name__ == "__main__":
    perpus = Perpustakaan("Perpustakaan STITEK")

    b1 = perpus.tambah_buku("Pemrograman Python", "Guido", "BK01", 3, "Rak A-1")
    b2 = perpus.tambah_buku("Struktur Data", "Wirth", "BK02", 2, "Rak A-2")
    b3 = perpus.tambah_buku("Basis Data", "Elmasri", "BK03", 4, "Rak B-1")

    a1 = Anggota("AG01", "Budi")
    a2 = Anggota("AG02", "Siti")

    a1.pinjam_buku(b1, "2026-11-25")
    a1.pinjam_buku(b2, "2026-11-25")
    a2.pinjam_buku(b3, "2026-11-25")
    a1.kembalikan_buku(b1, "2026-11-27")

    print("\n--- Informasi Buku ---")
    for b in perpus.koleksi_buku:
        print(f"{b.kode_buku} - {b.judul} ({b.penulis}) | Stok: {b._stok} | Lokasi: {b.get_lokasi_rak()}")

    print("\n--- Informasi Anggota ---")
    for a in [a1, a2]:
        print(f"{a.id_anggota} - {a.nama} | Maks Pinjam: {a._maks_pinjam} | Aktif: {a.get_status()}")

    print("\n--- Daftar Peminjaman ---")
    for a in [a1, a2]:
        print(f"{a.nama}:")
        for p in a.daftar_peminjaman:
            print(" -", p.info_peminjaman())