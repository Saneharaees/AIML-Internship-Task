import numpy as np
# Difference between Copy and View
arr = np.array([1, 2, 3, 4, 5])

# Copy (Independent)
x = arr.copy()
arr[0] = 42
# View (Dependent)
y = arr.view()
arr[1] = 100

print("Original:", arr)
print("Copy (No change):", x)
print("View (Reflects change):", y)
print("Does 'x' own data?", x.base) # None
print("Does 'y' own data?", y.base) # Returns original array
