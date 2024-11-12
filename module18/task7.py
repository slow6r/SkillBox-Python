# Многомерный список
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Раскрытие всех вложенных списков
flattened_list = [num for sublist1 in nice_list for sublist2 in sublist1 for num in sublist2]

# Вывод результата
print(flattened_list)
