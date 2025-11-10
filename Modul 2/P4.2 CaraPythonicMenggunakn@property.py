class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
    
        self.nilai = nilai 
    @property
    def nilai(self):
        print("(Memanggil getter @property)")
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai_baru):
        print(f"(Memanggil setter @nilai.setter dengan nilai {nilai_baru})")

        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid.")
susi = Siswa("Susi", 80)
print("-" * 20)

susi.nilai = 101
print("-" * 20)

susi.nilai = 90 
print("-" * 20)

print(f"Nilai Susi sekarang: {susi.nilai}")
