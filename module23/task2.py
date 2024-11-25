def print_reversed_zen(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())

print_reversed_zen('zen.txt')
