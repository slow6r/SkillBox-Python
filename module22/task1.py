def print_numbers(num, current=1):
    if current > num:
        return
    print(current)
    print_numbers(num, current + 1)

if __name__ == "__main__":
    num = int(input("Введите num: "))
    print_numbers(num)
