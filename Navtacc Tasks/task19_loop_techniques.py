# This script demonstrates various looping techniques in Python
# Exercise on various looping techniques in Python

# Using enumerate to get index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index} is {color}")

# Using zip to loop through two lists at once
names = ["Ali", "Sara"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
