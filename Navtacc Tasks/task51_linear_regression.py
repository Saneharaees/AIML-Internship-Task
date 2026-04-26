import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dataset: Salary prediction based on years of experience
# (Simulated Dataset)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) # Experience
y = np.array([30000, 35000, 47000, 52000, 60000, 65000, 68000, 75000, 82000, 90000]) # Salary

# Step 1: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 2: Create and Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Prediction
prediction = model.predict([[5.5]])
print(f"Predicted Salary for 5.5 years exp: {prediction[0]}")

# Step 4: Visualization
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Linear Regression: Salary vs Experience')
plt.show()
