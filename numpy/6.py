# Example 6: NumPy - 3D Array Indexing
import numpy as np
# Creating a 3D array
array_3d = np.array([[[1, 2,5], [3, 4,6]], [[7, 8, 9], [10, 11,12]]])

# Accessing element
element = array_3d[1, 0, 2] 

# Slicing row and column
slice_3d = array_3d[:, 0, :]

print('Element at (1,0,2):', element)
print('Sliced 3D Array:\n', slice_3d)