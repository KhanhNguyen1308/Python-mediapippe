import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
abalone_train = pd.read_csv(
    "data.csv",
    names=["x1", "x2", "x3", "x4", "x5", "x6", "mode"])
abalone_train.head()
abalone_features = abalone_train.copy()
print(abalone_features)
abalone_labels = abalone_features.pop('mode')
abalone_features = np.array(abalone_features)
abalone_model = tf.keras.Sequential([
  layers.Dense(64),
  layers.Dense(1)
])

abalone_model.compile(loss = tf.losses.MeanSquaredError(),
                      optimizer = tf.optimizers.Adam())
abalone_model.fit(abalone_features, abalone_labels, epochs=1000)
normalize = preprocessing.Normalization()
normalize.adapt(abalone_features)
norm_abalone_model = tf.keras.Sequential([
  normalize,
  layers.Dense(64),
  layers.Dense(1)
])

norm_abalone_model.compile(loss = tf.losses.MeanSquaredError(),
                           optimizer = tf.optimizers.Adam())
norm_abalone_model.fit(abalone_features, abalone_labels, epochs=1000)
norm_abalone_model.save('keras_model.h5')