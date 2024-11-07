def reverse_even_numbers():
    n = int(input("Введите количество чисел: "))
    numbers = [int(input("Введите число: ")) for _ in range(n)]
    print("Чётные числа в обратном порядке:")
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] % 2 == 0:
            print(numbers[i], end=' ')
    print()