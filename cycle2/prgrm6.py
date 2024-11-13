import numpy as np
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("The 2D Array")
print(array)
first_row_excluded = array[:1]
print("The array excluding first row:", first_row_excluded)
last_column_excluded = array[:, :-1]
print("The array excluding last column:\n", last_column_excluded)
column_1_2_and_row_2_3 = array[1:3, 0:2]
print("Elements of the 1st and 2nd column in the 2nd and 3rd row:\n", column_1_2_and_row_2_3)
column_2_3 = array[:, 1:3]
print("Elements of 2nd and 3rd column:\n", column_2_3)
elements_2_3_in_first_row = array[0, 1:3]
print("2nd and 3rd element of 1st row:\n", elements_2_3_in_first_row)
descending_order = array.ravel() [::-1] [4:11]
print("Elements from indices 4 to 10 in descending order:",descending_order)
