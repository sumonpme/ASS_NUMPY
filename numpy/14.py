# Example 14: NumPy - Using Ellipsis (...) in Indexing
import numpy as np
# Creating a 2D array
array_2d = np.array([ [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

result = array_2d[..., 1]  

print('Result using Ellipsis (...):\n', result)