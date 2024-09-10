N = int(input("Введите N: "))

total_sum = 0.0

for n in range(N):
    elem = (-1) ** n * (1/2) ** n
    total_sum += elem

print(f"Ответ: {total_sum:.6f}")
