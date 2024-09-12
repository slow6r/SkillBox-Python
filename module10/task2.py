N = int(input("Введите число N: "))

for i in range(1, N + 1):

    line = [str(i)] * i

    print(" ".join(line))
