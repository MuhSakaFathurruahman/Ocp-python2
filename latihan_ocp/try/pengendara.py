from karakter import Karakter

class Pengendara:
    
    def nama(self, karakter: Karakter)->str:
        return ("Namanya : ", karakter.get_nama())
    
    def kekutatan(self, karakter: Karakter)->int:
        return ("Power : ", karakter.get_power())
    
    
