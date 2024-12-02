import random


class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 50  # сытость
        self.health = 100  # здоровье
        self.money = 50    # деньги

    def eat(self):
        if self.money >= 10:
            self.satiety += 10
            self.money -= 10
            print(f"{self.name} поел. Сытость: {self.satiety}, Деньги: {self.money}")
        else:
            print(f"У {self.name} недостаточно денег для еды!")

    def work(self):
        self.satiety -= 10
        self.money += 20
        print(f"{self.name} работал. Сытость: {self.satiety}, Деньги: {self.money}")

    def play(self):
        self.satiety -= 5
        print(f"{self.name} играл. Сытость: {self.satiety}")

    def rest(self):
        self.health += 10
        self.satiety -= 5
        print(f"{self.name} отдохнул. Здоровье: {self.health}, Сытость: {self.satiety}")

    def is_alive(self):
        return self.satiety > 0 and self.health > 0

class House:
    def __init__(self, *inhabitants):
        self.inhabitants = inhabitants

    def one_day(self):
        for person in self.inhabitants:
            if person.is_alive():
                action = random.choice(["eat", "work", "play", "rest"])
                getattr(person, action)()
            else:
                print(f"{person.name} умер.")
                self.inhabitants.remove(person)

human1 = Human("Алексей")
human2 = Human("Мария")
house = House(human1, human2)

for day in range(1, 8):
    print(f"\nДень {day}")
    house.one_day()
