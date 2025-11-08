# Building  Convolutional Neural Network (CNN) Model

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input

# load MNIST dataset
mnist = tf.keras.datsets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize pixel values (0-255) to (0-1) for better performance
X_train, X_test = X_test / 255.0, X_test / 255.0

# build the CNN model
model = Sequential([
    Input(shape=(28, 28, 1)), 
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# model summary
model.summary()

# Display a smaple digit
# plt.imshow(X_train[0], cmap="gray")
# plt.title(f"label: {y_train[0]}")
# plt.show()

