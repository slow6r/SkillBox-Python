n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))
people = list(range(1, n + 1))
index = 0

while len(people) > 1:
    index = (index + k - 1) % len(people)
    print(f"Выбывает человек под номером {people[index]}")
    people.pop(index)

print(f"Остался человек под номером {people[0]}")
