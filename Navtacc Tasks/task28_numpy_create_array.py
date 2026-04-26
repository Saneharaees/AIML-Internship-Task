import numpy as np
# Creating arrays using different methods
arr1 = np.array([1, 2, 3, 4, 5]) # 1D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # 2D Array
arr3 = np.zeros((3, 3)) # 3x3 Zero matrix
arr4 = np.ones((2, 4)) # 2x4 One matrix
arr5 = np.arange(0, 10, 2) # Range array [0, 2, 4, 6, 8]

print("1D Array:\n", arr1)
print("2D Array Shape:", arr2.shape)
print("Zeros Matrix:\n", arr3)
