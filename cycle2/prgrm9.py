import numpy as np
array_1d = np.array([1, 2, 3, 4])
print("1D Array:\n", array_1d)
diagonal_1d = np.diag(array_1d)
print("1D Array Diagonal Matrix:\n", diagonal_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", array_2d)
diagonal_2d = np.diag(array_2d)
print("2D Array Diagonal Elements:\n", diagonal_2d)

array_2d_non_square = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Non-square Array:\n", array_2d_non_square)
diagonal_non_square = np.diag(array_2d_non_square)
print("Diagonal Elements(Non-sqaure):\n", diagonal_non_square)
