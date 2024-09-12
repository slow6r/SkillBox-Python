pirates_on_board = 0

for i in range(10):
    word = input(f"Введите слово {i + 1}: ").strip()
    if word.lower() == "карамба":
        pirates_on_board += 1

print(f"На борт попадет {pirates_on_board} человек(а)!")
