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