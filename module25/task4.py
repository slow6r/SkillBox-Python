class Element:
    def __add__(self, other):
        combinations = {
            ("Water", "Air"): "Storm",
            ("Water", "Fire"): "Steam",
            ("Water", "Earth"): "Mud",
            ("Air", "Fire"): "Lightning",
            ("Air", "Earth"): "Dust",
            ("Fire", "Earth"): "Lava"
        }
        result = combinations.get((self.name, other.name)) or combinations.get((other.name, self.name))
        return result or None

class Water(Element):
    name = "Water"

class Air(Element):
    name = "Air"

class Fire(Element):
    name = "Fire"

class Earth(Element):
    name = "Earth"

print(Water() + Air())  # Шторм
print(Fire() + Earth())  # Лава
print(Water() + Fire())  # Пар
