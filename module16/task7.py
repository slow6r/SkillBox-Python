def is_palindrome():
    word = input("Введите слово: ")
    if word == word[::-1]:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")