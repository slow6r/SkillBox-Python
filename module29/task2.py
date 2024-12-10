import math

class MyMath:
    """Класс для математических вычислений."""

    @staticmethod
    def circle_len(radius: float) -> float:
        """Вычисляет длину окружности."""
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius: float) -> float:
        """Вычисляет площадь круга."""
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(edge: float) -> float:
        """Вычисляет объём куба."""
        return edge ** 3

    @staticmethod
    def sphere_surface_area(radius: float) -> float:
        """Вычисляет площадь поверхности сферы."""
        return 4 * math.pi * radius ** 2

# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)