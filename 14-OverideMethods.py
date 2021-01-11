class Hero:
    def __init__(self, name, health):
        self.nama = name
        self.darah = health

    def showInfo(self):
        print("Nama Hero : {} Darah : {}".format(
            self.nama,
            self.darah
        ))


class Hero_intelegence(Hero):
    def __init__(self, name):
        super().__init__(name, 1200)

    # Overide
    def showInfo(self):
        print("Nama Hero : {} \n\t Type : Intelegence \n\tDarah : {}".format(
            self.nama,
            self.darah
        ))


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 1200)

    def showInfo(self):
        print("Nama Hero : {} \n\t Type : Strength \n\tDarah : {}".format(
            self.nama,
            self.darah
        ))


class Hero_Tank(Hero):
    def __init__(self, name):
        super().__init__(name, 2100)

    def showInfo(self):
        print("Nama Hero : {} \n\t Type : Tank \n\tDarah : {}".format(
            self.nama,
            self.darah
        ))


Kagura = Hero_intelegence("Kagura")
Kings = Hero_strength("Kings")
Asubu = Hero_Tank("Asubu")

Kagura.showInfo()
Kings.showInfo()
Asubu.showInfo()
