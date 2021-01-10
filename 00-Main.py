class Hero: #template
    pass

hero1 = Hero()  #object
hero2 = Hero()
hero3 = Hero()

hero1.name = "Wawah"
hero1.health = 100

hero2.name = "budi"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1.name)
print(hero1.__dict__)
print(hero2.health)
print("Nama Hero : ",hero1.name," - Dengan Darah : ",hero1.health)