import random

# Генерация двух списков случайных чисел
team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

# Генерация списка победителей
winners = [max(a, b) for a, b in zip(team1, team2)]

# Вывод результатов
print("Первая команда:", team1)
print("Вторая команда:", team2)
print("Победители тура:", winners)
