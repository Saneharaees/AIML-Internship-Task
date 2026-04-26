import numpy as np
# Splitting arrays
arr = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 parts
new_arr = np.array_split(arr, 3)
print("Split into 3:", new_arr)

# Splitting 2D array
arr2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
new_2d = np.array_split(arr2d, 2)
print("Split 2D into 2 parts:\n", new_2d)
