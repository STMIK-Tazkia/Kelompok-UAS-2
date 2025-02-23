#tugas uts Bagian 1 soal No 1
import numpy as np

# Matriks A dan B diberikan
A = np.array([
    [10, 23, 21, 11],
    [55, 5, 7, 88],
    [34, 22, 21, 32],
    [10, 14, 11, 15]
])

B = np.array([
    [1, 0, 8, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 8, 0, 1]
])

# Perkalian matriks A x B
C = np.dot(A, B)

# Menampilkan hasil
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nHasil A x B:")
print(C)