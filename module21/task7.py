def custom_zip(iterable1, iterable2):
    return ((iterable1[i], iterable2[i]) for i in range(min(len(iterable1), len(iterable2))))

# Пример
string = "abcd"
numbers = (10, 20, 30, 40)

zipped = custom_zip(string, numbers)
print(zipped)
for pair in zipped:
    print(pair)
