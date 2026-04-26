import numpy as np
# Standard Deviation aur Variance
# Ye batata hai ke data 'mean' se kitna phaila hua hai
speed = [86, 87, 88, 86, 87, 85, 86]

std_dev = np.std(speed)
variance = np.var(speed)

print("Speed Data:", speed)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
# Low Standard Deviation ka matlab hai data mean ke qareeb hai
