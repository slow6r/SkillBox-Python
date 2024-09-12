milk_per_stall = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

stalls = input("Введите строку из 10 символов, где 'a' — свободное стойло, 'b' — занятое: ")

if len(stalls) != 10:
    print("Ошибка: строка должна содержать ровно 10 символов.")
else:
    total_milk = 0

    for i in range(10):
        if stalls[i] == 'b':
            total_milk += milk_per_stall[i]

    print(f"Всего молока за день: {total_milk} литров.")
