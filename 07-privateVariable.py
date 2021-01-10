class Hero:

    jumlah = 0 # class Variabel
    __privateJumlah = 0

    def __init__(self,name,health):
        self.nama = name
        self.darah = health
    # Variable instance private 
        self.__private = 'private'
    # variable intance protected
        self._protected = "protected"

lina = Hero("Lina",100)

print(lina.__dict__)
print(Hero.__dict__)

