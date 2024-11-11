num_rollers = int(input("Количество роликов: "))
rollers = [int(input(f"Размер пары {i + 1}: ")) for i in range(num_rollers)]

num_people = int(input("Количество людей: "))
people = [int(input(f"Размер ноги человека {i + 1}: ")) for i in range(num_people)]

rollers.sort()
people.sort()
count = 0

i, j = 0, 0
while i < len(rollers) and j < len(people):
    if rollers[i] >= people[j]:
        count += 1
        j += 1
    i += 1

print(f"Наибольшее количество людей, которые могут взять ролики: {count}")
