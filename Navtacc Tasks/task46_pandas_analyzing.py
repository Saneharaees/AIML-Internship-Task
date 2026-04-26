import pandas as pd
# Data Analysis functions
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Head (First 5):\n", df.head())
print("\nTail (Last 5):\n", df.tail())
print("\nInfo about data:")
df.info() # Data types aur missing values batata hai
