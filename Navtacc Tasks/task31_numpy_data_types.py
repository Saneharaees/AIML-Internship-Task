import numpy as np
# Checking and defining data types
arr = np.array([1, 2, 3, 4], dtype='i4') # Integer 4 bytes
arr_float = arr.astype('f') # Converting to float

print("Integer Array Type:", arr.dtype)
print("Converted Float Array Type:", arr_float.dtype)

string_arr = np.array(['apple', 'banana'], dtype='S')
print("String Array Type:", string_arr.dtype)
