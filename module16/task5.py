def container_placement():
    n = int(input("Количество контейнеров: "))
    containers = [int(input("Введите вес контейнера: ")) for _ in range(n)]
    new_weight = int(input("Введите вес нового контейнера: "))
    position = 1
    for weight in containers:
        if new_weight <= weight:
            position += 1
    print("Номер, который получит новый контейнер:", position)