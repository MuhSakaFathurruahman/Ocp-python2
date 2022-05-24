from karakter import Karakter
from menyerang import Menyerang

class Pengendara(Karakter, Menyerang):
    
    def kendara(self, karakter: Karakter):
        return karakter.get_nama(), karakter.get_power()
    
    def nyerang(Menyerang):
        print("Menabrakan diri")