def print_odd_number_pyramid(levels):
    current_number = 1
    
    for i in range(1, levels + 1):

        spaces = levels - i
        numbers = ' '.join(str(current_number + 2 * j) for j in range(i))
        current_number += 2 * i
        
        line = ' ' * spaces + numbers
        print(line)

def main():

    levels = int(input("Введите количество уровней пирамиды: "))
    
    if levels < 1:
        print("Количество уровней должно быть положительным числом.")
    else:
        print_odd_number_pyramid(levels)

main()
