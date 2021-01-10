class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.power = attackPower
        self.armor = armorNumber

    def serang(self,Lawan):
        print(self.name + ' Menyerang ' + Lawan.name) 
        Lawan.diserang(self,self.power)
    
    def diserang(self,Lawan,attackPower_Lawan):
        print(self.name + ' Diserang ' + Lawan.name)
        diterima = attackPower_Lawan/self.armor
        print('attack terasa : ' + str(diterima))
        self.health -= diterima
        print("Darah : " + self.name + " Tersisa : " + str(self.health) )

Sniper = Hero('sniper',100,10,5)
Rikimaru = Hero('Rikimaru',100,20,10)
 
Sniper.serang(Rikimaru)
print('\n')
Rikimaru.serang(Sniper)
