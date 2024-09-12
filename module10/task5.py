def sum_of_digits(number):

    return sum(int(digit) for digit in str(number))

def main():
    N = int(input("Введите количество чисел: "))
    
    max_sum = 0
    number_with_max_sum = None
    
    for _ in range(N):
        number = int(input("Введите число: "))
        current_sum = sum_of_digits(number)
        
        if current_sum > max_sum:
            max_sum = current_sum
            number_with_max_sum = number
    
    if number_with_max_sum is not None:
        print(f"Число с наибольшей суммой цифр: {number_with_max_sum}")
        print(f"Сумма его цифр: {max_sum}")
    else:
        print("Не было введено ни одного числа.")

main()
