initial_buckwheat = 100
monthly_consumption = 4

for month in range(1, (initial_buckwheat // monthly_consumption) + 1):
    remaining_buckwheat = initial_buckwheat - month * monthly_consumption
    print(f"Через {month} месяц(а) у вас останется {remaining_buckwheat} кг гречки.")

print("Гречка закончилась!")
