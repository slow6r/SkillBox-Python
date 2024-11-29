def chat():
    user_name = input("Введите ваше имя: ")
    
    while True:
        print("\nДоступные действия:")
        print("1. Посмотреть текущий текст чата")
        print("2. Отправить сообщение")
        print("0. Выйти из чата")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                with open('chat.txt', 'r', encoding='utf-8') as file:
                    print("\nТекущий чат:\n")
                    print(file.read())
            except FileNotFoundError:
                print("Чат пока пуст.")
        elif choice == "2":
            message = input("Введите сообщение: ")
            with open('chat.txt', 'a', encoding='utf-8') as file:
                file.write(f"{user_name}: {message}\n")
        elif choice == "0":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск функции
chat()
