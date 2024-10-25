try:
    x = float(input('Введите число: '))
    if x <= 0:
        raise ValueError('Число должно быть больше нуля.')
except ValueError as e:
    print("Ошибка ввода:", e)
    
else:
    
    b = 0
    
    if x >= 10:
        while x >= 10:
            x /= 10
            b += 1
            
    elif x < 1:
        while x < 1:
            x *= 10
            b -= 1
            
    print (f"Формат плавающей точки: x = {x} * 10 ** {b}")
            
            

    


