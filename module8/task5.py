start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))

def f(x):
    return x**2 + 1

for x in range(start, end + step, step):
    print(f"В точке {x} функция равна {f(x)}")
