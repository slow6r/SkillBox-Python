def print_pit_pattern(n):
    for i in range(n-1, -1, -1):
        left_part = ''.join(str(j) for j in range(n, n - i - 1, -1))
        
        spaces = '.' * (2 * i)
        
        right_part = ''.join(str(j) for j in range(n - i, n + 1))
        
        print(left_part + spaces + right_part)

def main():
    n = int(input("Введите число N: "))
    
    if n < 1:
        print("Число должно быть положительным.")
    else:
        print_pit_pattern(n)

main()
