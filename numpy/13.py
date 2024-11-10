# Example 13: NumPy - Indexing Multi-dimensional Arrays with Slices
import numpy as np

# Creating a 2D array (matrix)
array_2d = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8], 
                     [9, 10, 11, 12]])

sliced_array = array_2d[1:2, 3:4]

print("Sliced 2D Array:")
print(sliced_array)
