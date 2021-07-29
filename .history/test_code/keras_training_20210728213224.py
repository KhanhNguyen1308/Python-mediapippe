import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
pose_train = pd.read_csv(
    "data.csv",
    names=["x1", "x2", "x3", "x4", "x5", "x6", "mode"])
pose_train.head()
pose_features = pose_train.copy()
print(pose_features)
pose_labels = pose_features.pop('mode')
pose_features = np.array(pose_features)
pose_model = tf.keras.Sequential([
  layers.Dense(64),
  layers.Dense(1)
])

pose_model.compile(loss = tf.losses.MeanSquaredError(),
                      optimizer = tf.optimizers.Adam())
pose_model.fit(pose_features, pose_labels, epochs=1000)
normalize = preprocessing.Normalization()
normalize.adapt(pose_features)
norm_pose_model = tf.keras.Sequential([
  normalize,
  layers.Dense(64),
  layers.Dense(1)
])

norm_pose_model.compile(loss = tf.losses.MeanSquaredError(),
                           optimizer = tf.optimizers.Adam())
norm_pose_model.fit(pose_features, pose_labels, epochs=1000)
norm_pose_model.save('keras_model.h5')