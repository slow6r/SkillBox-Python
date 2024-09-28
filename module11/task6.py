knight_x = float(input("Введите местоположение коня (координата x): "))
knight_y = float(input("Введите местоположение коня (координата y): "))
target_x = float(input("Введите местоположение точки на доске (координата x): "))
target_y = float(input("Введите местоположение точки на доске (координата y): "))

knight_cell = (int(knight_x * 4), int(knight_y * 4))
target_cell = (int(target_x * 4), int(target_y * 4))

can_move = ((abs(knight_cell[0] - target_cell[0]) == 2 and abs(knight_cell[1] - target_cell[1]) == 1) or
            (abs(knight_cell[0] - target_cell[0]) == 1 and abs(knight_cell[1] - target_cell[1]) == 2))

print(f"Конь в клетке {knight_cell}. Точка в клетке {target_cell}.")
print("Да, конь может ходить в эту точку." if can_move else "Нет, конь не может ходить в эту точку.")
