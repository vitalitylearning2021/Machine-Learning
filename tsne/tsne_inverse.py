# -*- coding: utf-8 -*-
"""tsne_inverse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GksHpi4lCcdZDbLFDtQnMPWGkPDVbmLK
"""

import numpy as np
from sklearn.manifold import TSNE
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# 1. Data loading and pre-processing
(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# 2. Application of t-SNE to get a reduced (2D) representation
tsne = TSNE(n_components=2, random_state=42)
x_train_tsne = tsne.fit_transform(x_train)

# 3. Definition of the decoding net (attempt to reconstruct the original data)
input_tsne = Input(shape=(2,))
x = Dense(128, activation='relu')(input_tsne)
x = Dense(256, activation='relu')(x)
x = Dense(512, activation='relu')(x)
output_img = Dense(28*28, activation='sigmoid')(x)

decoder = Model(inputs=input_tsne, outputs=output_img)
decoder.compile(optimizer='adam', loss='mse')

# 4. Network training
decoder.fit(x_train_tsne, x_train, epochs=50, batch_size=128, validation_split=0.2)

# 5. Visualization of the reconstructed images
n = 10  # Number of original images to visualize
decoded_imgs = decoder.predict(x_train_tsne[:n])

# Show the original and reconstructed images
plt.figure(figsize=(20, 4))
for i in range(n):
    # Original images
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_train[i].reshape(28, 28), cmap='gray')
    plt.title("Original")
    plt.axis('off')

    # Reconstructed images
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28), cmap='gray')
    plt.title("Reconstructed")
    plt.axis('off')

plt.show()
