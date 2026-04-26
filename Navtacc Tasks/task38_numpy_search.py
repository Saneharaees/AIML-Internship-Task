import numpy as np
# Searching in arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])

# Find indexes where value is 4
x = np.where(arr == 4)
print("Indexes of 4:", x)

# Find indexes where values are even
even = np.where(arr % 2 == 0)
print("Even number indexes:", even)

# Search Sorted (finds index where element should be inserted)
arr_sorted = np.array([6, 7, 8, 9])
idx = np.searchsorted(arr_sorted, 7)
print("Insert 7 at index:", idx)
