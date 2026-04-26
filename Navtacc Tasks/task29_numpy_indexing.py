import numpy as np
# Accessing elements in NumPy arrays
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print("Element at [0,0]:", arr[0, 0])
print("Last element of 2nd row:", arr[1, -1])
# Advanced indexing
print("Elements at specific indices:", arr[[0, 1, 2], [0, 2, 1]]) # (0,0), (1,2), (2,1)
