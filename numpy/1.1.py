# Example 1: NumPy - Basic Indexing and Slicing
import numpy as np
# Creating a 2D array
array_2d = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])

# Accessing elements by index
first_element = array_2d[0, 2]   
last_element = array_2d[-1]      

# Slicing the array
slice_array = array_2d[0:2, 1:2]  

print('First Element:', first_element)
print('Last Element:', last_element)
print('Sliced Array:\n', slice_array)
