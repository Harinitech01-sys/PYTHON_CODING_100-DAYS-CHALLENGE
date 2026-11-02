import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

(x_train,_),(x_test,_)=tf.keras.datasets.mnist.load_data()


x_train=x_train.astype('float32')/255.0

x_test=x_test.astype('float32')/255.0
x_train=x_train.reshape(-1,784)
x_test=x_test.reshape(-1,784)
input_img=tf.keras.Input(shape=(784,))
encoded=tf.keras.layers.Dense(64,activation='relu')(input_img)
decoded=tf.keras.layers.Dense(784,activation='sigmoid')(encoded)
autoencoder=tf.keras.Model(input_img,decoded)


autoencoder.compile(optimizer='adam',loss='mse')
autoencoder.fit(x_train, x_train, epochs=5, batch_size=256)

reconstructed = autoencoder.predict(x_test)
plt.imshow(reconstructed[0].reshape(28, 28), cmap='gray')
plt.show()

plt.subplot(1,2,1)
plt.imshow(x_test[0].reshape(28,28), cmap='gray')
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(reconstructed[0].reshape(28,28), cmap='gray')
plt.title("Reconstructed")

plt.show()