import numpy as np
# Sorting arrays
arr = np.array([3, 2, 0, 1])
print("Sorted 1D:", np.sort(arr))

arr2d = np.array([[10, 5, 8], [50, 20, 30]])
print("Sorted 2D (row-wise):\n", np.sort(arr2d))

str_arr = np.array(['banana', 'cherry', 'apple'])
print("Sorted Strings:", np.sort(str_arr))
