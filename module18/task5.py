# Ввод строки
text = input("Введите строку: ")

# Поиск индексов первой и последней буквы 'h'
first_h = text.index('h')
last_h = text.rindex('h')

# Разворот подстроки между первым и последним 'h'
reversed_substring = text[first_h + 1:last_h][::-1]

# Вывод результата
print("Развёрнутая последовательность между первым и последним h:", reversed_substring)
