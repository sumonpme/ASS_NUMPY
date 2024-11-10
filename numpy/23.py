# Example 23: NumPy - Multi-dimensional Array Indexing with Mixed Types
import numpy as np

# Creating a 2D array 
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])

row_indices = np.array([0, 1])  
colms_slice = slice(1, 2)  

# mixed indexing
indexed_array = array_2d[row_indices, colms_slice]

print("\nArray after mixed indexing :")
print(indexed_array)
