import pandas as pd
# Deep dive into Series
# Labels ke saath Series banana
calories = {"day1": 420, "day2": 380, "day3": 390}
my_series = pd.Series(calories)

print("Series with Labels:\n", my_series)
print("\nAccessing day1:", my_series["day1"])
print("Mean calories:", my_series.mean())
