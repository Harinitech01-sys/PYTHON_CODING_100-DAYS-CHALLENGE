import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

(x, _), _ = tf.keras.datasets.mnist.load_data()
x = (x.astype("float32") - 127.5) / 127.5
x = tf.data.Dataset.from_tensor_slices(x[..., None])
x = x.shuffle(60000).batch(128)

G = tf.keras.Sequential([
    layers.Input(shape=(100,)),
    layers.Dense(7*7*128),
    layers.Reshape((7, 7, 128)),
    layers.Conv2DTranspose(64, 4, strides=2, padding="same"),
    layers.LeakyReLU(0.2),
    layers.Conv2DTranspose(1, 4, strides=2, padding="same", activation="tanh")
])

D = tf.keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(64, 4, strides=2, padding="same"),
    layers.LeakyReLU(0.2),
    layers.Flatten(),
    layers.Dense(1)
])

loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)
go = tf.keras.optimizers.Adam(0.0002, beta_1=0.5)
do = tf.keras.optimizers.Adam(0.0002, beta_1=0.5)

for epoch in range(30):
    for real in x:
        noise = tf.random.normal([128, 100])
        with tf.GradientTape() as gt, tf.GradientTape() as dt:
            fake = G(noise, training=True)
            real_out = D(real, training=True)
            fake_out = D(fake, training=True)
            gl = loss(tf.ones_like(fake_out), fake_out)
            dl = loss(tf.ones_like(real_out), real_out) + loss(tf.zeros_like(fake_out), fake_out)

        go.apply_gradients(zip(gt.gradient(gl, G.trainable_variables), G.trainable_variables))
        do.apply_gradients(zip(dt.gradient(dl, D.trainable_variables), D.trainable_variables))

    print("Epoch:", epoch+1, "Generator Loss:", float(gl), "Discriminator Loss:", float(dl))

noise = tf.random.normal([25, 100])
images = G(noise, training=False)

plt.figure(figsize=(7, 7))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.imshow(images[i, :, :, 0], cmap="gray", vmin=-1, vmax=1)
    plt.axis("off")
plt.show()