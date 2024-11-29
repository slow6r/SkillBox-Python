import math

def calculate_square_root():
    try:
        number = float(input("Введите число: "))
        if number < 0:
            raise ValueError("Невозможно вычислить квадратный корень из отрицательного числа.")
        result = math.sqrt(number)
        print(f"Квадратный корень числа {number} равен {result}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск функции
calculate_square_root()
