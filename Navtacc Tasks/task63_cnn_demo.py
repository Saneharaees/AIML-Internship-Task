from tensorflow.keras import layers, models
# Convolutional Neural Network (CNN) Structure
model = models.Sequential()
# Convolution Layer (Feature extraction)
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
# Flattening to pass to Dense layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.summary()
print("\nCNN Architecture defined successfully.")
