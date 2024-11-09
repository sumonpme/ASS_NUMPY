# Example 28: NumPy - Conditional Replacement with np.where
import numpy as np

# Creating an array
array_1d= np.array([20, 25, 30, 40, 50])
result = np.where(array_1d > 30, 0, array_1d)

print('Array with Values Greater Than 20 Replaced with 0:', result)