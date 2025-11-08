# Loading and Preprocessing the MNIST Dataset

import tensorflow as tf
import matplotlib.pyplot as plt

# load MNIST dataset
mnist = tf.keras.datsets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize pixel values (0-255) to (0-1) for better performance
X_train, X_test = X_test / 255.0, X_test / 255.0

# Display a smaple digit
plt.imshow(X_train[0], cmap="gray")
plt.title(f"label: {y_train[0]}")
plt.show()