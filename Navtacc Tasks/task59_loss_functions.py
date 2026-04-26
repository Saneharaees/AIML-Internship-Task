import tensorflow as tf
# Demonstrating different loss functions
y_true = [[0, 1]] # One-hot encoded
y_pred = [[0.2, 0.8]]

# 1. Categorical Crossentropy (For Multi-class)
cce = tf.keras.losses.CategoricalCrossentropy()
print("Categorical Crossentropy:", cce(y_true, y_pred).numpy())

# 2. Mean Squared Error (For Regression)
mse = tf.keras.losses.MeanSquaredError()
print("MSE Loss:", mse([10.0], [9.5]).numpy())

# 3. Binary Crossentropy (For Yes/No)
bce = tf.keras.losses.BinaryCrossentropy()
print("Binary Crossentropy:", bce([1], [0.1]).numpy())
