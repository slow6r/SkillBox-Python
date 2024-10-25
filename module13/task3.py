a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

a_reversed = int(str(a)[::-1])
b_reversed = int(str(b)[::-1])

print(f"Первое число наоборот {a_reversed}")
print(f"Второе число наоборот {b_reversed}")

sum_reversed = a_reversed + b_reversed

print(f"Сумма: {sum_reversed}")

sum = int(str(sum_reversed)[::-1])

print (f"Сумма наоборот: {sum}")



