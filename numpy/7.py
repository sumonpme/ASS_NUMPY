# Example 7: NumPy - Indexing with Arrays
import numpy as np

# 2D array
array_2d = np.array([[40, 50, 60, 100], 
                     [70, 80, 90, 110]])

# row and column indices
rows = np.array([0, 1])
colms = np.array([2, 0])
indexed_elements = array_2d[rows, colms]

print('Indexed Elements:', indexed_elements)
