import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# Dataset: Synthetic non-linear data (Moons)
X, y = make_moons(n_samples=1000, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Multi-Layer Perceptron (MLP) Model
model = Sequential([
    Dense(10, activation='relu', input_shape=(2,)),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid') # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("Training MLP on Moons Dataset...")
model.fit(X_train, y_train, epochs=50, verbose=0)
print(f"Test Accuracy: {model.evaluate(X_test, y_test, verbose=0)[1]}")
