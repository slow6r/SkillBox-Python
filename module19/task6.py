text = input("Введите строку: ")
compressed_text = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed_text += text[i - 1] + str(count)
        count = 1
compressed_text += text[-1] + str(count)

print("Закодированная строка:", compressed_text)
