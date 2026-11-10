import tensorflow as tf

# Create tensors
a = tf.constant([10, 20, 30])
b = tf.constant([1, 2, 3])

# Perform operations
print("Addition:", tf.add(a, b))
print("Multiplication:", tf.multiply(a, b))
print("Sum:", tf.reduce_sum(a))

# Create variable
w = tf.Variable(5.0)
w.assign(10.0)
print("Updated:", w.numpy())

import tensorflow as tf

# Define a variable
x = tf.Variable(3.0)

# Record mathematical operations
with tf.GradientTape() as tape:
    y = x ** 2

# Calculate derivative
gradient = tape.gradient(y, x)

print("Output:", y.numpy())
print("Gradient:", gradient.numpy())

