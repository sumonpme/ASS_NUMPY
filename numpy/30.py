# Example 30: NumPy - Combining Multiple Indexing Techniques
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]])

array = array_2d > 5
filtered_array = np.where(array, array_2d, 0)  
result = filtered_array[:, [0, 1]]

print("Combined Indexing Result:\n", result)
