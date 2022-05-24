class Karakter():
    def __init__(self, nama: str, power: int):
        self.__nama = nama
        self.__power = power
    
    def set_nama(self, nama: str)->None:
        self.__nama = nama
        
    def set_power(self, power: int)->None:
        self.__power = power
        
    def get_nama(self)-> str:
        return self.__nama
        
    def get_power(self)-> int:
        return self.__power