x = 8
y = 10
max_x = 15
max_y = 20

while True:
    print(f"Марсоход находится на позиции {x}, {y}. Введите команду:")
    command = input().upper()

    if command == "W" and y < max_y:
        y += 1
    elif command == "S" and y > 1:
        y -= 1
    elif command == "A" and x > 1:
        x -= 1
    elif command == "D" and x < max_x:
        x += 1
    else:
        print("Движение в эту сторону невозможно. Марсоход упёрся в стену.")

    if command == "Q":
        print("Завершение работы марсохода.")
        break
