class RekeningBank:
    def _init_(self, nama, saldo):
        self.nama = nama         # public
        self.__saldo = saldo     # private

    # method untuk menampilkan saldo
    def lihat_saldo(self):
        print(f"Saldo {self.nama}: {self.__saldo}")

akun_budi = RekeningBank("Budi", 1000000)
akun_budi.lihat_saldo()  # ✅ Bisa, karena lewat method dalam class

print(akun_budi.nama)    # ✅ Bisa, karena public
try:
    print(akun_budi.__saldo) # ❌ ERROR, karena saldo bersifat private
except Exception :
    print("anda tidak boleh mengakses saldo")