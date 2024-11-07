def sort_numbers():
    n = int(input("Введите количество чисел: "))
    numbers = [int(input("Введите число: ")) for _ in range(n)]
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Отсортированный список:", numbers)