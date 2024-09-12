text = input("Введите текст: ")

position = text.find('*') + 1  
if position > 0:
    print(f"Символ «*» стоит на позиции {position}.")
else:
    print("Символ «*» не найден в строке.")
