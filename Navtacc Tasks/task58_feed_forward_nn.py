import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Feed Forward Neural Network for XOR Problem
# Inputs
X = np.array([[0,0], [0,1], [1,0], [1,1]])
# XOR Outputs
y = np.array([[0], [1], [1], [0]])

model = Sequential([
    Dense(8, input_dim=2, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=0)

print("XOR Predictions:")
print(model.predict(X).round())
