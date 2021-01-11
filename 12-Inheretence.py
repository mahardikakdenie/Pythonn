class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health


class Hero_intelegence(Hero):
    pass

class Hero_strength(Hero):
    pass

lina = Hero("Lina",100)
exe = Hero_intelegence('exe',50)
wawah = Hero_strength("Wawah",200)
print(lina.name)
print(exe.name)
print(wawah.name)