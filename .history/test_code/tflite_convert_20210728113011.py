import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model("test/saved_model.pb")
tflite_model = converter.convert()
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)