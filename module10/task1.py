def print_table():
    start_rows = [0, 1, 2, 3, 5] 
    num_columns = 6  

    for start in start_rows:
        row = []
        for i in range(num_columns):
            row.append(start + 2 * i)
            
        print("\t".join(map(str, row)))

print_table()
