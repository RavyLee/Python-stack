import random

# Функция для генерации матрицы с заданными размерами
def generate_matrix(rows, cols):
    return [[random.randint(-200, 200) for _ in range(cols)] for _ in range(rows)]

# Функция для сложения двух матриц
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Генерация двух матриц 10x10
matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

# Сложение матриц
matrix_3 = add_matrices(matrix_1, matrix_2)

# Печать матриц для проверки результата
print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nMatrix 3 (Result of Addition):")
for row in matrix_3:
    print(row)
