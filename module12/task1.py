def summa_n(n):
    total = sum(range(1, n + 1))
    print(f"Я знаю, что сумма чисел от 1 до {n} равна {total}")

n = int(input("Введите число: "))
summa_n(n)
