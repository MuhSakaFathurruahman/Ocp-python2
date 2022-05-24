from karakter import Karakter
from pengendara import Pengendara

class Shower:
    def show_nama(self, karakter: Karakter, pengendara: Pengendara):
        print(pengendara.nama(karakter))
        
    def show_power(self, karakter: Karakter, pengendara: Pengendara):
        print(pengendara.kekutatan(karakter))