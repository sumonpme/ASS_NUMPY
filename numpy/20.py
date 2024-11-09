# Example 20: NumPy - Cumulative Sum and Product
import numpy as np
# Create a 1D array
array_1d = np.array([5, 10, 15, 20, 25, 30])
cumulative_sum = np.cumsum(array_1d)
cumulative_product = np.cumprod(array_1d)

print("Cumulative Sum:", cumulative_sum)
print("Cumulative Product:", cumulative_product)
