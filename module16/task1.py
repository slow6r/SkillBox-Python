def generate_odd_numbers():
    n = int(input("Введите число: "))
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
    print("Список из нечётных чисел от одного до N:", odd_numbers)