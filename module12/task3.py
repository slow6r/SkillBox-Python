def sum_digits(num):
    return sum(int(digit) for digit in str(num))

def max_digit(num):
    return max(int(digit) for digit in str(num))

def min_digit(num):
    return min(int(digit) for digit in str(num))

def calculator():
    while True:
        num = int(input("Введите число: "))
        action = input("Что сделать с числом (сумма/макс/мин)? ")
        
        if action == "сумма":
            print(f"Сумма цифр числа: {sum_digits(num)}")
        elif action == "макс":
            print(f"Максимальная цифра числа: {max_digit(num)}")
        elif action == "мин":
            print(f"Минимальная цифра числа: {min_digit(num)}")

calculator()
