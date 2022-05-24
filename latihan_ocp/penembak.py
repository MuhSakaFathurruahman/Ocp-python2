from karakter import Karakter
from menyerang import Menyerang

class Penembak(Karakter, Menyerang):
    
    def tembak(self, karakter: Karakter)->float:
        super().__init__(nama, power)
        
    def nyerang(self):
        print(F"{self.nama}Menembak")