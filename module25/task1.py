import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, other):
        damage = 20
        other.health -= damage
        print(f"{self.name} атакует {other.name}. У {other.name} осталось {other.health} здоровья.")

def fight(warrior1, warrior2):
    while warrior1.health > 0 and warrior2.health > 0:
        attacker = random.choice([warrior1, warrior2])
        defender = warrior1 if attacker == warrior2 else warrior2
        attacker.attack(defender)
        if defender.health <= 0:
            print(f"{attacker.name} одержал победу!")
            break

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

fight(warrior1, warrior2)
