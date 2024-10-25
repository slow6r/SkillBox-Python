def danger_level(x):
    """Вычисляет уровень опасности D по заданной формуле."""
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(tolerance):
    """Находит безопасную глубину, при которой уровень опасности близок к нулю."""
    low = 0  
    high = 4 
    mid = 0 

    while high - low > tolerance: 
        mid = (low + high) / 2
        if danger_level(mid) > 0:
            high = mid 
        else:
            low = mid 

    return (low + high) / 2  

def main():
    while True:
        try:
            tolerance = float(input("Введите максимально допустимый уровень опасности: "))
            if tolerance <= 0:
                print("Допустимый уровень опасности должен быть положительным числом.")
                continue
            break
        except ValueError:
            print("Введите корректное число.")

    safe_depth = find_safe_depth(tolerance)
    print(f"Приблизительная глубина безопасной кладки: {safe_depth:.9f} м")

if __name__ == "__main__":
    main()
