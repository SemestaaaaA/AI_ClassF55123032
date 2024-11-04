import numpy as np

# Membuat matriks 2x3
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])

# Membuat matriks 3x4
matrix_b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

# Perkalian matriks 2x3 dengan 3x4
matrix_product = np.dot(matrix_a, matrix_b)

# Menampilkan hasil
print("Matrix A (2x3):")
print(matrix_a)
print("\nMatrix B (3x4):")
print(matrix_b)
print("\nHasil perkalian Matrix A dan B:")
print(matrix_product)


