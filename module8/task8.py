X = int(input("Введите количество мальчиков: "))
Y = int(input("Введите количество девочек: "))

if abs(X - Y) > 1:
    print("Нет решения")
else:
    result = []
    if X >= Y:
        while X > 0 or Y > 0:
            if X > 0:
                result.append('B')
                X -= 1
            if Y > 0:
                result.append('G')
                Y -= 1
    else:
        while X > 0 or Y > 0:
            if Y > 0:
                result.append('G')
                Y -= 1
            if X > 0:
                result.append('B')
                X -= 1

    print("".join(result))
