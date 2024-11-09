# Example 12: NumPy - Combining Boolean and Fancy Indexing
import numpy as np

# Creating an array
array_1d = np.array([10, 20, 30, 40, 50, 60])
filtered_array= array_1d[(array_1d<50) & (array_1d> 20)] 
result= filtered_array[[0, 1]]
print('Combined Boolean and Fancy Indexing Result:', result)