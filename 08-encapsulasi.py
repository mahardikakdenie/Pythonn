class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attpower = attackPower

    # Getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # Setter
    def diserang(self,attPower):
        self.__health -= attPower
    
    def setattPower(self,nilaiBaru):
        self.__attpower = nilaiBaru


earthShaker = Hero('earthShaker',50,5)

# Awal Dari Game
print(earthShaker.__dict__)

# Game Berjalan
print(earthShaker.getName())
print(earthShaker.getHealth())
earthShaker.diserang(5)
print(earthShaker.getHealth())

