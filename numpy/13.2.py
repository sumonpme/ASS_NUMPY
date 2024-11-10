# Example 13: NumPy - Statistical Functions
import numpy as np
# Creating an array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Calculating statistical values
mean = np.mean(array_1d)
median = np.median(array_1d)
std_dev = np.std(array_1d)
variance = np.var(array_1d)

print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)
print('Variance:', variance)