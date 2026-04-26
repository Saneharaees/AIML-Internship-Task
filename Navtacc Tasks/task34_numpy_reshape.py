import numpy as np
# Changing shape of arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape to 2D (4 rows, 3 columns)
new_arr = arr.reshape(4, 3)
# Reshape to 3D
arr_3d = arr.reshape(2, 3, 2)

print("2D Reshaped:\n", new_arr)
print("3D Reshaped:\n", arr_3d)
# Flattening the array back to 1D
print("Flattened:", arr_3d.reshape(-1))
