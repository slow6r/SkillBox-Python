def maximum_of_two(a, b):
    return a if a > b else b

def maximum_of_three(x, y, z):
    max_of_first_two = maximum_of_two(x, y)
    
    return maximum_of_two(max_of_first_two, z)

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_value = maximum_of_three(num1, num2, num3)
print(f"Максимальное из трёъ чисел: {max_value}")