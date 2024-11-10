# Example 21: NumPy - Reverse Array using Indexing
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5, 6, 7])

# Reversing the 1D array using slicing
reversed_1d = array_1d[::-3]
print(reversed_1d)