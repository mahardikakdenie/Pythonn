class Hero: #template
    
    def __init__(self,inputName,inputHealth,inpuPower,inputArmor):
        self.name =  inputName
        self.health = inputHealth
        self.power = inpuPower
        self.armor = inputArmor

hero1 = Hero("Wawah",100,100,10000)
hero2 = Hero("Mirana",100,1000,1000)
hero3 = Hero("Ucup",100,10000,100)
print("Nama : ",hero1.name," Health : ",hero1.health,"  Power : ",hero1.power," Armor : ",hero1.armor)
print("Nama : ",hero2.name," Health : ",hero2.health,"  Power : ",hero2.power," Armor : ",hero2.armor)
print("Nama : ",hero3.name," Health : ",hero3.health,"  Power : ",hero3.power," Armor : ",hero3.armor)

