class Hero:
    def __init__(self,name,health):
        self.nama = name
        self.darah = health
    def ShowInfo(self):
        print("Nama Hero : {} dengan Health : {} ".format(self.nama,self.darah))
class Hero_intelegence(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,100)
        super().__init__(name,100)
        super().ShowInfo()

class Hero_strength(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,200)
        super().__init__(name,200)
        super().ShowInfo()

Udin = Hero_intelegence("Udin")
Baba = Hero_strength("Baba")


