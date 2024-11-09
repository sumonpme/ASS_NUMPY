#Example 2: NumPy - 2D Array Indexing
import numpy as np
# Creating a 2D array
array_2d = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

# Accessing individual elements
element = array_2d[0, 2]  

# Slicing rows and columns
row_slice = array_2d[0, :]  
column_slice = array_2d[:, 1]  

print('Element at (0,2):', element)
print('First Row:', row_slice)
print('Second Column:', column_slice)