import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
import matplotlib.pyplot as plt
from google.colab import files

#picture size 224 pixel
SIZE = 224

#get data set
#the second information is _, and is not relevant. It's for example size
train, _ = tfds.load('cats_vs_dogs', split=['train[:100%]'], with_info=True, as_supervised=True)

#walk through  first 10 images
for img, label in train[0].take(10):
  plt.figure()
  plt.imshow(img)
  print(label)

def resize_image(img, label):
 img = tf.cast(img, tf.float32)
 img = tf.image.resize(img, (SIZE, SIZE))
 img = img / 255.0
 return img, label

train_resized = train[0].map(resize_image)
train_batches = train_resized.shuffle(1000).batch(16)