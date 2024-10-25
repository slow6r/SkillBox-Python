def main():
    """Основная функция, выполняющая логику программы."""
    
    while True:
        try:
            initial_amplitude = float(input("Введите начальную амплитуду (в см): "))
            if initial_amplitude <= 0:
                raise ValueError("Амплитуда должна быть положительным числом.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            final_amplitude = float(input("Введите амплитуду остановки (в см): "))
            if final_amplitude <= 0:
                raise ValueError("Амплитуда остановки должна быть положительным числом.")
            break
        except ValueError as e:
            print(e)

    count = 0
    current_amplitude = initial_amplitude

    while current_amplitude > final_amplitude:
        current_amplitude *= (1 - 0.084) 
        count += 1

    print(f"Маятник считается остановившимся через {count} колебаний.")

if __name__ == "__main__":
    main()
