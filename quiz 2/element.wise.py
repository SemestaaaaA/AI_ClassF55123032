import numpy as np

# Definisikan matriks A (2x3) dan B (2x3)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

# Perkalian elemen per elemen
elementwise_product = A * B

# Menampilkan matriks dan hasil perkalian
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nElement-wise Product of A and B:")
print(elementwise_product)
