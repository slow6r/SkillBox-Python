def is_prime(number):

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    count = int(input("Введите количество чисел: "))
    
    prime_count = 0
    
    for _ in range(count):
        number = int(input("Введите число: "))
        if is_prime(number):
            prime_count += 1
    
    print(f"Количество простых чисел в последовательности: {prime_count}")

main()
