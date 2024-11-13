import numpy as np
array = np.arange(2, 31, 2)
print("Array with the first 15 even numbers")
print(array)
slice_array = array[2:9:2]
print("Numbers from index 2 to 8:", slice_array)
last_3 = array[-3:]
print("Last 3 elements:", last_3)
alternate = array[::2]
print("Alternate elements of Array:", alternate)
last3_alt = alternate[-3:]
print("Last 3 Alternate elements:", last3_alt)
