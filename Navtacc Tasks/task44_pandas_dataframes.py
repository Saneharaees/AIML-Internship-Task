import pandas as pd
# DataFrames: Rows aur Columns ka structure
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

# loc attribute ka use (rows access karne ke liye)
print("Row 0 data:\n", df.loc[0])
print("\nRows 0 and 1:\n", df.loc[[0, 1]])
