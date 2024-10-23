def reverse_number(num):
    reversed_num = str(num)[::-1]
    print(f"Число наоборот: {reversed_num}")

while True:
    num = int(input("Введите число: "))
    if num == 0:
        print("Программа завершена!")
        break
    reverse_number(num)
