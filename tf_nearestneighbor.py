# -*- coding: utf-8 -*-
"""TF_NearestNeighbor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sBvZ9KWHDIDh05mIqRHp15i9ie7woAP8
"""

import tensorflow as tf
import numpy as np

numTests            = 128     # --- Number of actually used test database
numIter             = 1000    # --- Number of gradient descent iterations
shuffleBufferSize   = 5000    # --- Buffer size for shuffling the input data 
batchSize           = 256     # --- Batch size for the train data

numClasses          = 10      # --- Number of classes of the MNIST dataset (0 to 9 digits)
numFeatures         = 784     # --- Number of features (each image is a 28 x 28 image, 
                              #     to be flattened to a row of 784 elements)
                              
# --- Load MNIST dataset
from tensorflow.keras.datasets import mnist
(xTrain, yTrain), (xTest, yTest) = mnist.load_data()

# --- The dataset (xTrain, xTest, yTrain, yTest) has uint8 type. We need to cast it to float32.
xTrain, xTest = np.array(xTrain, np.float32), np.array(xTest, np.float32)

# --- The images are 28 x 28, so we flatten them to 1-D vectors of 784 features.
xTrain, xTest = xTrain.reshape([-1, numFeatures]), xTest.reshape([-1, numFeatures])

# --- The image values range from 0 to 255. We normalize them to [0, 1].
xTrain, xTest = xTrain / 255., xTest / 255.

# --- Slices the data row-wise and takes batches out of them
trainData = tf.data.Dataset.from_tensor_slices((xTrain, yTrain))
trainData = trainData.repeat().shuffle(shuffleBufferSize).batch(batchSize).prefetch(1)

xTest = xTest[0 : numTests, :]
xTest = tf.convert_to_tensor(xTest)

for iter, (featuresBatch, classesBatch) in enumerate(trainData.take(numIter), 1):

  if (iter > 1):
    featuresBatch = tf.concat([featuresBatch, featurePredictions], 0)
    classesBatch  = tf.concat([classesBatch,  classesPredictions], 0)
  
  expandedTrain                 = tf.expand_dims(featuresBatch, 0)
  expandedTest                  = tf.expand_dims(xTest, 1)

  distance                      = tf.reduce_sum(tf.square(tf.subtract(expandedTrain, expandedTest)), 2)

  pred                          = tf.argmin(distance, 1)

  featurePredictions            = tf.gather(featuresBatch, pred, axis = 0)
  classesPredictions            = tf.gather(classesBatch, pred, axis = 0)

  accuracy                      = 100. * np.sum(yTest[0 : numTests] == classesPredictions) / numTests
  
  print('accuracy {}'.format(accuracy))