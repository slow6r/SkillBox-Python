def build_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def invert_frequency(freq):
    inverted = {}
    for char, count in freq.items():
        inverted.setdefault(count, []).append(char)
    return inverted

text = input("Введите текст: ")
freq = build_frequency(text)
print("Оригинальный словарь частот:", freq)
print("Инвертированный словарь частот:", invert_frequency(freq))
