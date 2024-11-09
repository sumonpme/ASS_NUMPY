# Example 29: NumPy - Using np.choose for Multiple Conditions
import numpy as np

array_1d = np.array([5, 10,15, 20, 25, 30, 35])
conditions = [
    array_1d < 10,          
    (array_1d >= 15) & (array_1d < 35),  
    array_1d >= 35        
]
choices = [
    -1,     
    0,      
    1      
]
result = np.choose([cond.astype(int) for cond in conditions], choices)

print("Original Array:", array_1d)
print("Result after applying np.choose:", result)
