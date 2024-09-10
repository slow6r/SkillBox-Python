reverse_timer = int(input("Введите время до обнуления таймера (в секундах): "))

for seconds_left in range(reverse_timer, 0, -1):
    user_input = input(f"Осталось {seconds_left} секунд. Хотите остановить разогрев? (Введите 1 для остановки, 0 для продолжения): ")
    if user_input == '1':
        print(f"Ваша еда готова, можете забрать. Таймер был прерван на {seconds_left} секунд(е).")
        break
else:
    print("Ваша еда готова, осторожно горячо!")
