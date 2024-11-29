import random

def lucky_number():
    total_sum = 0

    try:
        with open('out_file.txt', 'w', encoding='utf-8') as file:
            while total_sum < 777:
                user_input = int(input("Введите число: "))
                
                # Проверка на вероятность 1 к 13
                if random.randint(1, 13) == 1:
                    raise Exception("Вас постигла неудача!")
                
                total_sum += user_input
                file.write(f"{user_input}\n")
                
            print("Вы успешно выполнили условие для выхода из порочного цикла!")
    except Exception as e:
        print(e)

# Запуск функции
lucky_number()
