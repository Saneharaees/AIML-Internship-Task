# This script demonstrates how to use the continue statement to skip iterations
# Exercise on Continue statement in Python

for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print("Number:", i)
