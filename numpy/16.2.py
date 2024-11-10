# Example 16: NumPy - Splitting Arrays
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Split the array
split_arr = np.array_split(array_1d, 2)
print(split_arr)
