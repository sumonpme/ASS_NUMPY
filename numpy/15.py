# Example 15: NumPy - Concatenation of Arrays
import numpy as np
# Creating arrays
array_1 = np.array([1, 2, 3,4, 5])
array_2 = np.array([6, 7, 8, 9, 10])

# Concatenating arrays
concatenated_array = np.concatenate((array_1, array_2))

print('Concatenated Array:', concatenated_array)