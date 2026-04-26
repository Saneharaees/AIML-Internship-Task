import pandas as pd
# Pandas Series aur DataFrame ki basics
data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# Dictionary se DataFrame banana
student_data = {
    'RollNo': [101, 102, 103],
    'Marks': [85, 90, 78],
    'Grade': ['B', 'A', 'C']
}
df = pd.DataFrame(student_data)

print("Pandas Series:\n", series)
print("\nPandas DataFrame:\n", df)
