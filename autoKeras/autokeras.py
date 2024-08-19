# -*- coding: utf-8 -*-
"""autoKeras.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tT8UwnxONXP0ERkKzFqMUMuk0Jh1G5Sl
"""

pip install tensorflow autokeras

import tensorflow as tf
from tensorflow.keras.datasets import mnist
import autokeras as ak

# Load the MNIST data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Reshape the data to fit the model input requirements
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Initialize the ImageClassifier
clf = ak.ImageClassifier(
    max_trials=2,  # Number of different models to try
    overwrite=True  # Overwrite the previous results
)

# Train the model with the training data
clf.fit(x_train, y_train, epochs=4)

# Evaluate the model on the test data
loss, accuracy = clf.evaluate(x_test, y_test)
print(f"Test accuracy: {accuracy:.4f}")

# Export the best model
model = clf.export_model()

# Save the model
model.save("best_mnist_model.h5")

print(model.summary())