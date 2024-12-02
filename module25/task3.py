class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Дети: {[child.name for child in self.children]}")

    def calm_child(self, child):
        print(f"{self.name} успокаивает {child.name}")
        child.is_calm = True

    def feed_child(self, child):
        print(f"{self.name} кормит {child.name}")
        child.is_hungry = False


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_calm = False
        self.is_hungry = True

parent = Parent("Иван", 40)
child1 = Child("Маша", 10)
child2 = Child("Саша", 8)

parent.add_child(child1)
parent.add_child(child2)
parent.info()

parent.feed_child(child1)
parent.calm_child(child2)
