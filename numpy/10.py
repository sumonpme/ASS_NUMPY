# Example 10: NumPy - Modifying Array Values using Indexing
import numpy as np

# Creating an array
array_1d = np.array([1, 2, 7, 8, 9, 10])

array_1d[2:4] = [20, 30]  

print('Modified Array:', array_1d)
