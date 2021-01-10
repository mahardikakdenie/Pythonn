class Hero:
    jumlah_Hero = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_Hero += 1

    # Void Methods
    def siapa(self):
        print("Nama Ku adalah " + self.name)
    
    # methods dengan argumen
    def healthUp(self,up):
        self.health += up

    # Methods Dengan Return
    def getHealth(self):
        return self.health 

Kaizuki = Hero('Kaizuki',100,10,100)
marioB = Hero('marioB',100,10,10)

Kaizuki.siapa()
Kaizuki.healthUp(200)
print(Kaizuki.getHealth())