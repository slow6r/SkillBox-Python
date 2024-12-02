class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(result)

    def __sub__(self, other):
        result = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other.data)] for self_row in self.data]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
        return Matrix(result)

# Пример использования
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

print("Матрица 1:")
print(matrix1)
print("\nМатрица 2:")
print(matrix2)

print("\nСумма матриц:")
print(matrix1 + matrix2)

print("\nРазность матриц:")
print(matrix1 - matrix2)

print("\nТранспонированная матрица 1:")
print(matrix1.transpose())
