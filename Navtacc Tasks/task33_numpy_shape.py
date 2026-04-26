import numpy as np
# Checking shape of arrays
arr1 = np.array([1, 2, 3, 4], ndmin=5) # 5-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("5D Array Shape:", arr1.shape)
print("2D Array Dimensions:", arr2.ndim)
print("Total elements in 2D array:", arr2.size)
