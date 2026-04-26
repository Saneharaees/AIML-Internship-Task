import pandas as pd
# Data Correlation (Variables ka aapas mein talluq)
data = {
  "Duration": [60, 60, 60, 45, 45],
  "Pulse": [110, 117, 103, 109, 117],
  "Calories": [409, 479, 340, 282, 306]
}
df = pd.DataFrame(data)

# Correlation matrix
print("Correlation Matrix:\n", df.corr())
# Note: 1.0 matlab strong relation, 0 matlab no relation
