# Example 9: NumPy - Broadcasting
import numpy as np

array_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

#Broadcasting
result= array_2d+5
print('Original Array:', array_2d)
print('Array after Broadcasting:', result)