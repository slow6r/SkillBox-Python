message = input("Введите фрагмент послания: ")

cleaned_message = message.replace(" ", "").lower()

if cleaned_message == cleaned_message[::-1]:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")
