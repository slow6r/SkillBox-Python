class Hero:
    def attack(self):
        raise NotImplementedError

class Tank(Hero):
    def attack(self):
        return "Tank attacks"

class Healer(Hero):
    def attack(self):
        return "Healer heals"

class Attacker(Hero):
    def attack(self):
        return "Attacker attacks"
