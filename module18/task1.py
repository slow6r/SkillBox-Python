# Ввод текста от пользователя
text = input("Введите текст: ")

# Определение гласных букв
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

# Генерация списка гласных в тексте
vowel_list = [char for char in text if char in vowels]

# Вывод результата
print("Список гласных букв:", vowel_list)
print("Длина списка:", len(vowel_list))
