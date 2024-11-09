# Example 12: NumPy - Boolean Indexing
import numpy as np
array_1d = np.array([2, 3, 4, 5, 6, 7, 8])

# Boolean indexing
even_numbers = array_1d[array_1d % 2 == 0]
odd_numbers = array_1d[array_1d % 2 == 1]

print('Original Array:', array_1d)
print('Even Numbers:', even_numbers)
print('Odd Numbers:', odd_numbers)