from numpy import random
import numpy as np
# Random numbers and distributions
x = random.randint(100) # Random int 0-100
y = random.rand(5) # 5 random floats 0-1

# Random array
arr_int = random.randint(100, size=(3, 5))
# Choice from a list
choice = random.choice([3, 5, 7, 9], size=(2, 3))

print("Random Integer Array:\n", arr_int)
print("Random Choice Matrix:\n", choice)
