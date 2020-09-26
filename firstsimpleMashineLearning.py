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

base_layers = tf.keras.applications.MobileNetV2(input_shape=(SIZE, SIZE, 3), include_top=False)
base_layers.trainable = False

model = tf.keras.Sequential([
                             base_layers,
                             GlobalAveragePooling2D(),
                             Dropout(0.2),
                             Dense(1)
])
model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])

model.fit(train_batches, epochs=1)

model.fit(train_batches, epochs=2)

files.upload()

for i in range(4):
  img = load_img(f'cat{i+2}.jpg')
  img_array = img_to_array(img)
  img_resized, _ = resize_image(img_array, _)
  img_expended = np.expand_dims(img_resized, axis=0)
  prediction = model.predict(img_expended)[0][0]
  pred_label = 'cat' if prediction < 0.5 else 'dog'
  plt.figure()
  plt.imshow(img)
  plt.title(f'{pred_label} {prediction}')