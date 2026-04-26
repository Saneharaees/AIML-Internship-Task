import numpy as np
# Joining arrays (Concatenate and Stack)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate
res = np.concatenate((arr1, arr2))
# Stacking (Horizontal, Vertical, Depth)
h_stack = np.hstack((arr1, arr2))
v_stack = np.vstack((arr1, arr2))

print("Concatenated:", res)
print("Horizontal Stack:", h_stack)
print("Vertical Stack:\n", v_stack)
