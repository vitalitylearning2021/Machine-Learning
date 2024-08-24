# -*- coding: utf-8 -*-
"""UAT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kudWmHwGzENYgXQ6CjDyMwElIuQaPrmx
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 1. Generate training data
np.random.seed(0)  # For reproducibility
x_train = np.random.uniform(0, 1, 1000)  # 1000 points in [0, 1]
y_train = x_train**2  # Target function y = x^2

# 2. Define the model
model = Sequential()
model.add(Dense(units=10, input_dim=1, activation='sigmoid'))  # Hidden layer with 10 neurons
model.add(Dense(units=1, activation='linear'))  # Output layer

# 3. Compile the model
model.compile(optimizer=Adam(learning_rate=0.01), loss='mean_squared_error')

# 4. Train the model
history = model.fit(x_train, y_train, epochs=1000, batch_size=32, verbose=0)

# 5. Generate test data
x_test = np.linspace(0, 1, 100)  # 100 points in [0, 1] for testing
y_test = x_test**2  # True function

# 6. Predict using the trained model
y_pred = model.predict(x_test)

# 7. Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, color='gray', label='Training Data')
plt.plot(x_test, y_test, color='blue', label='True Function $f(x) = x^2$')
plt.plot(x_test, y_pred, color='red', linestyle='--', label='NN Approximation')
plt.title('Neural Network Approximation of $f(x) = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()