# Example 3: NumPy - Boolean Indexing
import numpy as np
# Creating an array
array_1d = np.array([10, 20, 30, 40, 50])

# Boolean indexing
greater_than_30 = array_1d[array_1d > 30]

print('Elements Greater Than 20:', greater_than_30)
