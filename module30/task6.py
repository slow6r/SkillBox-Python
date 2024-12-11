import time
from typing import Callable

class LoggerDecorator:
    """Класс-декоратор для логирования аргументов, результатов и времени выполнения функции."""
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Результат: {result}")
        print(f"Время выполнения: {end_time - start_time:.5f} секунд")
        return result

@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            result += i + j
    return result

# Пример использования:
result = complex_algorithm(10, 50)
