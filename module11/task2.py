import math

N = int(input("Введите кол-во чисел: "))
for _ in range(N):
    number = float(input("Введите число: "))
    if number > 0:  
        rounded_number = math.ceil(number)
        result = math.log(rounded_number)
        print(f"x = {rounded_number} log(x) = {result}")
    else:
        rounded_number = math.floor(number)
        result = math.exp(rounded_number)
        print(f"x = {rounded_number} exp(x) = {result}")
