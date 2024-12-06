from typing import Iterator, Generator

# Класс-итератор
class SquareIterator:
    def __init__(self, n: int):
        self._n = n
        self._current = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._current > self._n:
            raise StopIteration
        result = self._current ** 2
        self._current += 1
        return result

# Функция-генератор
def square_generator(n: int) -> Generator[int, None, None]:
    for i in range(1, n + 1):
        yield i ** 2

# Генераторное выражение
def square_expression(n: int) -> Iterator[int]:
    return (i ** 2 for i in range(1, n + 1))

# Пример использования
n = int(input("Введите число N: "))
print("Класс-итератор:", list(SquareIterator(n)))
print("Функция-генератор:", list(square_generator(n)))
print("Генераторное выражение:", list(square_expression(n)))
