import pandas as pd
# Data Cleaning (Missing values handle karna)
data = {
    'Name': ['Ali', 'Sara', None, 'Zain'],
    'Age': [20, None, 22, 23],
    'Score': [85, 90, 78, None]
}
df = pd.DataFrame(data)

# Method 1: Remove rows with NULL values
clean_df = df.dropna()

# Method 2: Fill NULL values with a specific value
filled_df = df.fillna({'Age': 21, 'Score': 0, 'Name': 'Unknown'})

print("Original Data:\n", df)
print("\nCleaned Data (Removed NULLs):\n", clean_df)
print("\nFilled Data:\n", filled_df)
