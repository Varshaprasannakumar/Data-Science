import numpy as np
matrix_size=3
matrix = np.random.randint(10, 20, size=(matrix_size, matrix_size))
print("Original Matrix:\n", matrix)
if np.linalg.matrix_rank(matrix) == matrix_size:
    inverse_matrix = np.linalg.inv(matrix)
    print("Inverse Matrix:\n", inverse_matrix)
else:
    print("The matrix is not invertible (it's rank is less than the size).")
rank = np.linalg.matrix_rank(matrix)
print("\nRank of the Matrix:", rank)
determinant = np.linalg.det(matrix)
print("\nDeterminant of the Matrix:", determinant)
matrix_1d = matrix.flatten()
print("\nMatrix as 1D Array:")
print(matrix_1d)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
