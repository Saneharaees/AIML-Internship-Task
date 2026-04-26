import numpy as np
# Iterating through arrays using nditer
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Normal iteration through 3D (nested loops):")
for x in arr:
    for y in x:
        for z in y:
            print(z, end=' ')

print("\nUsing nditer (optimized):")
for x in np.nditer(arr):
    print(x, end=' ')
