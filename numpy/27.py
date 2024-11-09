# Example 27: NumPy - Advanced Indexing with Meshgrid
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Creating meshgrid 
A, B = np.meshgrid(a,b)
indices = np.vstack([A.ravel(), B.ravel()])

print('Indices for Meshgrid Advanced Indexing:\n', indices)