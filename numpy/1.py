# Example 1: NumPy - Array Creation Basics
import numpy as np
array_1d = np.array([1, 2, 3, 4, ])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
zeros_array = np.zeros((1, 2))  
ones_array = np.ones((2, 3))  
filled_array = np.full((3,3), 2)  
identity_matrix = np.eye(3) 
range_array = np.arange(0, 1, 2)  

print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Filled Array:\n", filled_array)
print("Identity Matrix:\n", identity_matrix)
print("Range Array:", range_array)





