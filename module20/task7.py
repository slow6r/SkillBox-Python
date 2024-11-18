array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Задача 1: элементы в каждом списке
common_no_sets = [x for x in array_1 if x in array_2 and x in array_3]
common_with_sets = list(set(array_1) & set(array_2) & set(array_3))

# Задача 2: элементы из первого списка, которых нет во втором и третьем
unique_no_sets = [x for x in array_1 if x not in array_2 and x not in array_3]
unique_with_sets = list(set(array_1) - set(array_2) - set(array_3))

print("Задача 1:")
print("Решение без множеств:", common_no_sets)
print("Решение с множествами:", common_with_sets)

print("\nЗадача 2:")
print("Решение без множеств:", unique_no_sets)
print("Решение с множествами:", unique_with_sets)
