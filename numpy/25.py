# Example 25: NumPy - Masked Indexing with np.ma.masked_where
import numpy as np
# Creating a 2D array
array_2d = np.array([[4, 5, 6], [7, 8, 9], [10, 12, 14]])

masked_array_2d = np.ma.masked_where(array_2d >=8, array_2d)

print("Masked 2D Array of masked):")
print(masked_array_2d)
