# Example 24: NumPy - Indexing with np.take
import numpy as np

array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]])

indices = [0, 2, 1]
result = np.take(array_2d, indices)
print("Selected Result:\n", result)