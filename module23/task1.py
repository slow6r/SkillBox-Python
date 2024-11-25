def calculate_sum(input_file, output_file):
    with open(input_file, 'r') as file:
        numbers = file.read().split()
    total = sum(map(int, numbers))
    
    with open(output_file, 'w') as file:
        file.write(str(total))

calculate_sum('numbers.txt', 'answer.txt')
