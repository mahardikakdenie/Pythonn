class Hero: #template
    # class Static
    jumlah = 0
    
    def __init__(self,inputName,inputHealth,inpuPower,inputArmor):
        # instance Variable
        self.name =  inputName
        self.health = inputHealth
        self.power = inpuPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat Hero Dengan Nama " + inputName)

hero1 = Hero("Wawah",100,100,10000)
print(Hero.jumlah)
hero2 = Hero("Mirana",100,1000,1000)
print(Hero.jumlah)
hero3 = Hero("Ucup",100,10000,100)
print(Hero.jumlah)
print("Nama : ",hero1.name," Health : ",hero1.health,"  Power : ",hero1.power," Armor : ",hero1.armor)
print("Nama : ",hero2.name," Health : ",hero2.health,"  Power : ",hero2.power," Armor : ",hero2.armor)
print("Nama : ",hero3.name," Health : ",hero3.health,"  Power : ",hero3.power," Armor : ",hero3.armor)