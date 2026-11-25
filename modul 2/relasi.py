# relasi aggregation
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # --- JAWABAN SOAL F (Method rata_rata pada class Mahasiswa) ---
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


if __name__ == "__main__":
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")

    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    # relasi association
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))

    def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
        print(f"Program Studi: {prodi.nama}")
        print("Matakuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
        print("Mahasiswa dan rata-rata nilai:")
        for m in semua_mahasiswa:
            relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
            if relevan:
                avg = sum(n.skor for n in relevan) / len(relevan)
                print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")
        print("-" * 40)

    # --- JAWABAN SOAL A (Tambah 2 Program Studi baru) ---
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_te = uni.buat_program("Teknik Elektro")

    # --- JAWABAN SOAL B (Tambah minimal 2 Mata Kuliah pada masing-masing Prodi baru) ---
    mk3 = MataKuliah("SI101", "Analisis Proses Bisnis")
    mk4 = MataKuliah("SI102", "Basis Data")
    prodi_si.tambah_matakuliah(mk3)
    prodi_si.tambah_matakuliah(mk4)

    mk5 = MataKuliah("TE101", "Rangkaian Listrik")
    mk6 = MataKuliah("TE102", "Sistem Digital")
    prodi_te.tambah_matakuliah(mk5)
    prodi_te.tambah_matakuliah(mk6)

    # --- JAWABAN SOAL C (Buat 3 Mahasiswa dan tambahkan objek Nilai) ---
    m3 = Mahasiswa("23003", "Andi")
    m4 = Mahasiswa("23004", "Rina")
    m5 = Mahasiswa("23005", "Dedi")

    m3.tambah_nilai(Nilai("SI101", 88))
    m3.tambah_nilai(Nilai("SI102", 92))
    m4.tambah_nilai(Nilai("TE101", 80))
    m4.tambah_nilai(Nilai("TE102", 84))
    m5.tambah_nilai(Nilai("TI101", 75))
    m5.tambah_nilai(Nilai("SI101", 82))

    semua_mhs = [m1, m2, m3, m4, m5]

    # --- JAWABAN SOAL D (Tampilkan daftar mata kuliah setiap Program Studi) ---
    print("=== DAFTAR MATA KULIAH PER PRODI ===")
    for p in uni.programs:
        daftar_mk = [f"{mk.kode} ({mk.nama})" for mk in p.daftar_matakuliah]
        print(f"{p.nama}: {', '.join(daftar_mk)}")
    print("-" * 40)

    # --- JAWABAN SOAL E (Tampilkan daftar nilai untuk setiap mahasiswa) ---
    print("=== DAFTAR NILAI MAHASISWA ===")
    for m in semua_mhs:
        nilai_str = [f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai]
        print(f"{m.nim} - {m.nama}: {', '.join(nilai_str)}")
    print("-" * 40)

    # --- JAWABAN SOAL F (Tampilkan rata-rata nilai setiap mahasiswa) ---
    print("=== RATA-RATA NILAI MAHASISWA ===")
    for m in semua_mhs:
        print(f"{m.nim} - {m.nama}: {round(m.rata_rata(), 2)}")
    print("-" * 40)

    # --- JAWABAN SOAL G (Panggil report_program untuk setiap Program Studi) ---
    print("=== REPORT SEMUA PROGRAM STUDI ===")
    for p in uni.programs:
        report_program(p, semua_mhs)