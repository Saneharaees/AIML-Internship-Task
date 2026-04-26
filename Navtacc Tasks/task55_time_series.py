import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Time Series: Analyzing patterns over time
# Creating a dummy Air Quality Index dataset
date_rng = pd.date_range(start='2026-01-01', end='2026-01-10', freq='H')
df = pd.DataFrame(date_rng, columns=['date'])
df['aqi_level'] = np.random.randint(50, 300, size=(len(date_rng)))
df.set_index('date', inplace=True)

print("Time Series Data Preview:\n", df.head())

# Rolling Mean (Trend analysis)
df['Moving_Average'] = df['aqi_level'].rolling(window=5).mean()

df.plot(figsize=(10,5))
plt.title("Time Series Analysis: AQI Trends")
plt.show()
