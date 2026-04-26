import numpy as np
# Slicing: [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Slice 1 to 5:", arr[1:5])
print("Last 3 elements:", arr[-3:])

# 2D Slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("First 2 rows, last 2 columns:\n", arr2d[:2, 1:])
