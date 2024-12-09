class SquaresIterator:
    def __init__(self, n: int):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Использование:
n = int(input("Введите число N: "))
squares_iter = SquaresIterator(n)
for square in squares_iter:
    print(square)
