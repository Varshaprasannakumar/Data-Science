import numpy as np
array_2d = np.array([[1+2j, 1+3j, 1+4j], [2+5j, 2+6j, 2+7j]], dtype=complex)
print("2D Array:")
print(array_2d)
rows, columns = array_2d.shape
print("Number of ROWS=", rows)
print("Number of COLUMNS=", columns)
dimensions = array_2d.ndim
print("Dimensions of the Array=", dimensions)
reshaped_array = array_2d.reshape(3, 2)
print("Reshaped Array(3*2):")
print(reshaped_array)
