# --- JAWABAN SOAL A ---
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk            # private

    # Getter & Setter protected
    def get_semester(self):
        return self._semester

    def set_semester(self, nilai):
        self._semester = nilai

    # Getter & Setter private
    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, nilai):
        self.__ipk = nilai


# --- JAWABAN SOAL B ---
m1 = Mahasiswa("23001", "Andi", 3, 3.65)
m2 = Mahasiswa("23002", "Siti", 5, 3.80)

print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())


# --- JAWABAN SOAL C ---
m1.set_semester(4)
m1.set_ipk(3.75)

m2.set_semester(6)
m2.set_ipk(3.90)

print("Setelah diubah:")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())