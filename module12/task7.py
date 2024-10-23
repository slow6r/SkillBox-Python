import random

def rock_paper_scissors():
    options = ["камень", "ножницы", "бумага"]
    user_choice = input("Введите камень, ножницы или бумага: ").lower()
    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

def guess_the_number():
    target = random.randint(1, 100)
    guess = 0
    while guess != target:
        guess = int(input("Угадайте число: "))
        if guess < target:
            print("Больше")
        elif guess > target:
            print("Меньше")
    print("Вы угадали!")

def mainMenu():
    while True:
        choice = input("Выберите игру (1 - Камень, ножницы, бумага, 2 - Угадай число, 0 - Выход): ")
        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            guess_the_number()
        elif choice == "0":
            print("Выход из программы.")
            break

mainMenu()
