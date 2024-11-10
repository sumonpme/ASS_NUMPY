# Example 22: NumPy - Extract Lower Triangle of a Matrix
import numpy as np
matrix = np.array([[4, 5, 6], [7, 8, 9]])

lower_triangle = np.tril(matrix)

print('Lower Triangle  Matrix:\n', lower_triangle)