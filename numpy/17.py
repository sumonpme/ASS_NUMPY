# Example 17: NumPy - Indexing with np.where()
import numpy as np
array_2d = np.array([[2, 4, 6], [8, 9, 11]])

# Finding indices even elements
even_indices = np.where(array_2d % 2== 0)
even_elements = array_2d[even_indices]

print("Indices of even elements:", even_indices)
print("Even elements:", even_elements)
