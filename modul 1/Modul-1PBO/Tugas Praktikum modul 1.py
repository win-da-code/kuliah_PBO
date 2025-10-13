# Membuat kelas PersegiPanjang
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # Method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar

    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


# Input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Membuat objek dari kelas PersegiPanjang
persegi = PersegiPanjang(panjang, lebar)

# Menampilkan hasil
print(f"Luas persegi panjang     : {persegi.hitung_luas()}")
print(f"Keliling persegi panjang : {persegi.hitung_keliling()}")
