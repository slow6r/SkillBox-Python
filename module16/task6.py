def rotating_numbers():
    n = int(input("Введите количество элементов в списке: "))
    numbers = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]
    shift = int(input("Сдвиг: ")) % n
    shifted_numbers = numbers[-shift:] + numbers[:-shift]
    print("Изначальный список:", numbers)
    print("Сдвинутый список:", shifted_numbers)