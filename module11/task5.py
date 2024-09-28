import math

earth_volume = 1.08321 * 10 ** 12 
radius = float(input("Введите радиус случайной планеты: "))
planet_volume = (4/3) * math.pi * (radius ** 3)

if planet_volume > earth_volume:
    ratio = planet_volume / earth_volume
    print(f"Объём планеты Земля меньше в {ratio:.3f} раз.")
else:
    ratio = earth_volume / planet_volume
    print(f"Объём планеты Земля больше в {ratio:.3f} раз.")
