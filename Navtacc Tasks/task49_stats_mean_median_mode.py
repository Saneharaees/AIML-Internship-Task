import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed, keepdims=True)

print("Data:", speed)
print("Mean (Average):", mean)
print("Median (Middle value):", median)
print("Mode (Most frequent):", mode.mode[0], "Frequency:", mode.count[0])
