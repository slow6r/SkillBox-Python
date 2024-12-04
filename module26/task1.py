class Property:
    def __init__(self, worth):
        self.__worth = worth

    @property
    def worth(self):
        return self.__worth

    @worth.setter
    def worth(self, value):
        if value < 0:
            raise ValueError("Стоимость не может быть отрицательной.")
        self.__worth = value

    def calculate_tax(self):
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах.")

class Apartment(Property):
    def calculate_tax(self):
        return self.worth / 1000

class Car(Property):
    def calculate_tax(self):
        return self.worth / 200

class CountryHouse(Property):
    def calculate_tax(self):
        return self.worth / 500

def main():
    money = float(input("Введите количество ваших денег: "))
    property_type = input("Введите тип имущества (apartment, car, countryhouse): ").lower()
    worth = float(input("Введите стоимость имущества: "))

    if property_type == "apartment":
        property_object = Apartment(worth)
    elif property_type == "car":
        property_object = Car(worth)
    elif property_type == "countryhouse":
        property_object = CountryHouse(worth)
    else:
        print("Некорректный тип имущества.")
        return

    tax = property_object.calculate_tax()
    print(f"Ваш налог на {property_type} составляет: {tax:.2f}")

    if money >= tax:
        print(f"У вас достаточно денег для уплаты налога.")
    else:
        print(f"Вам не хватает {tax - money:.2f} для уплаты налога.")

if __name__ == "__main__":
    main()
