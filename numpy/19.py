# Example 19: NumPy - Clipping Array Values
import numpy as np
# Creating an array
array_1d = np.array([4, 5, 6, 7, 8, 9])

clipped_array = np.clip(array_1d, 3, 7)

print('Original Array:', array_1d)
print('Clipped Array:', clipped_array)