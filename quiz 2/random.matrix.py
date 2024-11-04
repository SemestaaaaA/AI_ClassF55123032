import numpy as np

# Membuat matriks 2x3 dengan nilai acak dari 1 hingga 10
matrix_a = np.random.randint(1, 11, size=(2, 3))

# Membuat matriks 3x4 dengan nilai acak dari 1 hingga 10
matrix_b = np.random.randint(1, 11, size=(3, 4))

# Perkalian matriks 2x3 dengan 3x4
matrix_product = np.dot(matrix_a, matrix_b)

# Menampilkan hasil
print("Matrix A (2x3):")
print(matrix_a)
print("\nMatrix B (3x4):")
print(matrix_b)
print("\nHasil perkalian Matrix A dan B:")
print(matrix_product)
