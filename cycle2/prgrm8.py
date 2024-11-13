import numpy as np
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array before insertion:\n", array_1d)
array_1d = np.insert(array_1d, 2, 6)
print("1D Array after insertion:\n", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array before insertion:\n", array_2d)
array_2d = np.insert(array_2d, 1, [7, 8, 9], axis=0)
print("2D Array after insertion:\n", array_2d)
