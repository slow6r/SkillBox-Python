import random

# Первый способ
numbers = [random.randint(0, 99) for _ in range(10)]
pairs = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
print(f"Оригинальный список: {numbers}")
print(f"Новый список: {pairs}")

# Второй способ
from itertools import zip_longest

pairs = list(zip(numbers[::2], numbers[1::2]))
print(f"Новый список (альтернативный способ): {pairs}")
