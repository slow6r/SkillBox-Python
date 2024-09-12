rows = int(input("Введите количество рядов: "))
seats = int(input("Введите количество сидений в ряду: "))
space_between_rows = int(input("Введите количество метров между рядами: "))

for i in range(rows):
    row_with_seats = "=" * seats 
    space_between = " " + "*" * space_between_rows + " " 
    print(row_with_seats + space_between + row_with_seats)
