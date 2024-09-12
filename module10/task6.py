def print_pyramid(height):

    for i in range(1, height + 1):

        spaces = height - i
        hashes = 2 * i - 1

        line = ' ' * spaces + '#' * hashes
        print(line)

def main():

    height = int(input("Введите высоту пирамиды: "))
    
    if height < 1:
        print("Высота пирамиды должна быть положительным числом.")
    else:
        print_pyramid(height)

main()
