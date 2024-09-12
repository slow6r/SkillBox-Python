width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

if width < 2 or height < 2:
    print("Ширина и высота должны быть не менее 2.")
else:

    print('+' + '-' * (width - 2) + '+')
    
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    
    print('+' + '-' * (width - 2) + '+')
