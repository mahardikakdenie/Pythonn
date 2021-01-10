class Hero :

    def __init__(self,name,health,armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__info = "name {} : \n\thealth: {}".format(self.__name,self.__health) 

    @property
    def info(self):
        return self.__info
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input
    
    @armor.deleter
    def armor(self):
        self.__armor = None

print("Merubah Info")
sniper = Hero("Sniper",100,10)
print(sniper.info)

print("Getter dan Setter Untuk __armor: ")
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 20
print(sniper.armor)

print("Delete Armor : ")
del sniper.armor 
print(sniper.__dict__)
