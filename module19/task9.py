def count_uppercase_lowercase(text):
    uppercase_count = sum(1 for c in text if c.isupper())
    lowercase_count = sum(1 for c in text if c.islower())
    return uppercase_count, lowercase_count

text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
