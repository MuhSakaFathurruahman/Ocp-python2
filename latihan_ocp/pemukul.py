from karakter import Karakter
from menyerang import Menyerang

class Pemukul(Karakter, Menyerang):
    
    def pukul(self, karakter: Karakter)-> float:
        return karakter.get_nama(), karakter.get_power()
        
    def nyerang(Menyerang):
        print(F"{nama} Memukul {get_power()}")