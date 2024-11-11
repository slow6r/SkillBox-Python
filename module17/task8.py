sequence = list(map(int, input("Введите последовательность чисел: ").split()))

for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        additional_elements = sequence[:i][::-1]
        print(f"Нужно добавить элементов: {len(additional_elements)}")
        print("Сами элементы:", additional_elements)
        break
