class Hero:
    __jumlah = 0

    def __init__(self,name):
        self.__nama = name
        Hero.__jumlah += 1

    # Berlaku Untuk Objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # Methods Static
    @staticmethod
    def getterJumlah():
        return Hero.__jumlah
    
    @classmethod
    def getJml(cls):
        return cls.__jumlah

sniper = Hero("Sniper")
Reihan = Hero("Reihan")
Rikimaru = Hero("Rikimaru")
print(Hero.getJml())