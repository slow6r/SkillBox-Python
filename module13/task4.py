def count_numbers(num):
    """Получает число и возвращает количество цифр в числе."""
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp = temp // 10
    return count

def change_number(num):
    """Меняет в числе местами первую и последнюю цифры и возвращает изменённое число."""
    num_str = str(num)  
    if len(num_str) <= 1:  
        return num
    new_num_str = num_str[-1] + num_str[1:-1] + num_str[0]
    return int(new_num_str)  

def main():
    first_n = int(input("Введите первое число (не менее 3 цифр): "))
    first_num_count = count_numbers(first_n)
    
    if first_num_count < 3:
        print("Ошибка: В первом числе меньше трёх цифр.")
        return
    
    first_n = change_number(first_n)
    print('Изменённое первое число:', first_n)

    second_n = int(input("Введите второе число (не менее 4 цифр): "))
    second_num_count = count_numbers(second_n)

    if second_num_count < 4:
        print("Ошибка: Во втором числе меньше четырёх цифр.")
        return
    
    second_n = change_number(second_n)
    print('Изменённое второе число:', second_n)

    print('\nСумма чисел:', first_n + second_n)

if __name__ == "__main__":
    main()
