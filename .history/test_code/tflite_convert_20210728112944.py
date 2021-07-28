import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model("test/saved_model.pb")