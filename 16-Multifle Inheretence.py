class Team:
    def setTeam(self,team):
        self.team = team
    def ShowTeam(self):
        print(self.team)

class Tipe_Hero:
    def setType(self,type):
        self.type = type
    def showType(self):
        print(self.type)


class Hero(Team,Tipe_Hero):
    def __init__(self,name,health):
        self.name = name
        self.health = health

Ujang = Hero("Ujang",100)
Ujang.setTeam("MANCHESTER UNITED")
Ujang.setType("Merah")
Ujang.ShowTeam()
Ujang.showType()
