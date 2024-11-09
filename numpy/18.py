# Example 18: NumPy - Advanced Slicing with Step in 2D Array
import numpy as np
# Creating a 2D array
array_2d = np.array([[1, 2, 3, ], [ 6, 7, 8] ])

# Slicing  rows and columns
slice = array_2d[::2, ::2]

print('Advanced Sliced Array with Step:\n', slice)