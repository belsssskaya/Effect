import random
from functools import reduce

def input_matrix(n):
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = list(map(int, input(f"Введите значения элементов {i}-й строки через пробел: ").split()))
        matrix.append(row)
    return matrix

def generate_matrix(n):
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    return matrix

def sum_matrices(matrix1, matrix2):
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = sum(
            (-1) ** j * matrix[0][j] * determinant(sub_matrix(matrix, j))
            for j in range(size)
        )
        return det

def sub_matrix(matrix, j):
    return [row[:j] + row[j + 1:] for row in matrix[1:]]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def main():
    while True:
        print("Меню:")
        print("1. Ввод матрицы вручную")
        print("2. Сгенерировать матрицу")
        print("3. Решение")
        print("4. Выход")
        choice = input("Введите номер выбранного пункта: ")
        if choice == "1":
            n = int(input("Введите размерность матрицы: "))
            matrix1 = input_matrix(n)
            matrix2 = input_matrix(n)
            print("Матрица 1:")
            print_matrix(matrix1)
            print("Матрица 2:")
            print_matrix(matrix2)
        elif choice == "2":
            n = int(input("Введите размерность матрицы: "))
            matrix1 = generate_matrix(n)
            matrix2 = generate_matrix(n)
            print("Матрица 1:")
            print_matrix(matrix1)
            print("Матрица 2:")
            print_matrix(matrix2)
        elif choice == "3":
            try:
                sum_matrix = sum_matrices(matrix1, matrix2)
                det_matrix1 = determinant(sum_matrix)
                print("Сумма матриц:")
                print_matrix(sum_matrix)
                print("Определитель суммы матриц:")
                print(det_matrix1)
            except UnboundLocalError:
                print("Ошибка! Пожалуйста, сначала выберите пункт 1 или 2 для ввода или генерации матрицы.")
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт из меню (1-4).")
        print()

if __name__ == "__main__":
    main()