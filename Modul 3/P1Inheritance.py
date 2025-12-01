class Kendaraan:
    def __init__(self, nama):
        self.nama = nama
        print(f"Sebuah Kendaraan '{self.nama}' dibuat.")

    def maju(self):
        print(f"{self.nama} bergerak maju.")
        motor = Kendaraan ("motor vario")

class Mobil(Kendaraan):
    def putar_AC(self):
        print(f"{self.nama}: AC dinyalakan, sejuk!")

print("--- Membuat Object Mobil ---")
avanza = Mobil("Avanza Putih") 
avanza.maju() 
avanza.putar_AC()

print("--- Membuat objek kendaraan ---")
Motor = Kendaraan ("motor vario")
Motor.puter_AC()