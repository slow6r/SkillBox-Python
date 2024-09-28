a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
largest = a * ((a - b) / (a - b + abs(a - b))) + b * ((b - a) / (a - b + abs(a - b)))
print(f"Наибольшее число: {largest}")
