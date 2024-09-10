a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))

numbers = [x for x in range(a, b + 1) if x % c == 0]

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Числа в отрезке [{a}; {b}], кратные {c}: {numbers}")
    print(f"Среднее арифметическое: {average:.2f}")
else:
    print(f"Нет чисел в отрезке [{a}; {b}], кратных {c}.")
