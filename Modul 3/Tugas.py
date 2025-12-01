class Pegawai:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok   # atribut private

    # getter gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # bonus default (nanti dioverride)
    def hitung_bonus(self):
        return 0

    # getter gaji total
    def get_gaji_total(self):
        return self.__gaji_pokok + self.hitung_bonus()

    # tampilkan info dasar
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.__gaji_pokok:,}".replace(",", "."))


# ==============================
#        MANAGER
# ==============================
class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    def hitung_bonus(self):
        return int(self.get_gaji_pokok() * 0.15)# 15%

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,}".replace(",", "."))
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,}".replace(",", "."))


# ==============================
#        STAFF TEKNIS
# ==============================
class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek

    def hitung_bonus(self):
        return 500_000 * self.jumlah_proyek

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,}".replace(",", "."))


# ==============================
#        OBJEK
# ==============================
manager = Manager("Budi Hartono", "M-001", 10_000_000, 5_000_000)
staff = StaffTeknis("Susi Susanti", "S-001", 6_000_000, 3)

# ==============================
#        OUTPUT TUGAS
# ==============================
print("--- Info Manager ---")
manager.tampilkan_info()

print("\n" + "="*30 + "\n")

print("--- Info Staff Teknis ---")
staff.tampilkan_info()

print("\n" + "="*30 + "\n")

# ==============================
#        TES ENKAPSULASI
# ==============================
print("--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff.__gaji_pokok)
except Exception as e:
    print("ERROR:", e)
    print("-> TIDAK BISA diakses langsung dari luar!")

print(f"Gaji Total Susi (tetap): Rp {staff.get_gaji_total():,}".replace(",", ".")) 

