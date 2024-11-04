import numpy as np

# Membuat matriks 2x3
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])

# Membuat matriks 3x4
matrix_b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Perkalian matriks 2x3 dengan 3x4
matrix_product = np.dot(matrix_a, matrix_b)

# Menampilkan hasil
print("Percobaan Makmul") 
print("Matrix A (2x3):")
print(matrix_a)
print("\nMatrix B (3x4):")
print(matrix_b)
print("\nHasil perkalian Matrix A dan B:")
print(matrix_product)

import numpy as np

# Definisikan matriks A (2x3) dan B (2x3)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

# Perkalian elemen per elemen
elementwise_product = A * B

# Menampilkan matriks dan hasil perkalian
print("---------------------- ")
print("Percobaan element wise") 
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nElement-wise Product of A and B:")
print(elementwise_product)
