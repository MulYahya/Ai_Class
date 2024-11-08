#menggunakan pustaka numpy

import numpy as np

A = np.array([
    [2, 0, -3],
    [1, 4, 5]
])

B = np.array([
    [3, 1],
    [-1, 0],
    [4, 2]
])

C = np.array([
    [4, 7],
    [2, 1],
    [1, -1]
])


AB = np.dot(A, B)
AC = np.dot(A, C)

result = AB + AC

print("Hasil dari (AB + AC) adalah:\n", result)


#Tanpa pustaka numpy


def multiply_matrices(X, Y):

    rows_X, cols_X = len(X), len(X[0])
    rows_Y, cols_Y = len(Y), len(Y[0])
    

    if cols_X != rows_Y:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
    

    result = [[0 for _ in range(cols_Y)] for _ in range(rows_X)]
    

    for i in range(rows_X):
        for j in range(cols_Y):
            for k in range(cols_X):
                result[i][j] += X[i][k] * Y[k][j]
    
    return result


def add_matrices(X, Y):

    rows, cols = len(X), len(X[0])
    
 
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    

    for i in range(rows):
        for j in range(cols):
            result[i][j] = X[i][j] + Y[i][j]
    
    return result


A = [
    [2, 0, -3],
    [1, 4, 5]
]

B = [
    [3, 1],
    [-1, 0],
    [4, 2]
]

C = [
    [4, 7],
    [2, 1],
    [1, -1]
]


AB = multiply_matrices(A, B)
AC = multiply_matrices(A, C)


result = add_matrices(AB, AC)

print("Hasil dari (AB + AC) adalah:")
for row in result:
    print(row)
