class Hero:
    # private VARIABLE
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__experience = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return"\n{} : \n\tLevel : {}  \n\thealth : {}/{} \n\tAttack : {} \n\tArmor : {} \n".format(self.__name,self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__experience += addExp
        if (self.__experience >= 100):
            print(self.__name, " Level Up")
            self.__level += 1
            self.__experience -= 100
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self,musuh):
        self.gainExp = 50


Wawah = Hero("Wawah", 100, 10, 10)
Budi = Hero("Budi",100,20,10)
print(Wawah.info)

Wawah.attack(Budi)
Wawah.attack(Budi)
Wawah.attack(Budi)
print(Wawah.info)