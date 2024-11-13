str1 = input("Первая строка: ")
str2 = input("Вторая строка: ")

if len(str1) == len(str2) and str1 in str2 * 2:
    shift = (str2 * 2).index(str1)
    print(f"Первая строка получается из второй со сдвигом {shift}.")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
