# Example 15: NumPy - Masked Indexing
import numpy as np

# Creating a 2D array
array_2d = np.array([[4, 5, 6], [7, 8, 9], [10, 12, 14]])

masked_array_2d = array_2d[(array_2d > 7) & (array_2d <= 10)]

print("Masked 2D Array:", masked_array_2d)

