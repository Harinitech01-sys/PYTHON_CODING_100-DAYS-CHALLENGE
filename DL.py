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

# 1. Import libraries
import numpy as np
import tensorflow as tf

# 2. Create input data
# Features: Study hours, Attendance
X = np.array([
    [1, 40],
    [2, 50],
    [3, 60],
    [4, 70],
    [5, 80],
    [6, 90],
    [7, 95],
    [8, 98]
], dtype=float)

# 3. Output labels
# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# 4. Normalize attendance
X[:, 1] = X[:, 1] / 100

# 5. Create neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 6. Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 7. Train the model
model.fit(X, y, epochs=100, verbose=0)

# 8. Evaluate the model
loss, accuracy = model.evaluate(X, y, verbose=0)

print("Loss:", loss)
print("Accuracy:", accuracy)

# 9. Predict a new student
new_student = np.array([[6, 0.85]])

prediction = model.predict(new_student, verbose=0)

# 10. Display output
print("Prediction:", prediction[0][0])

if prediction[0][0] >= 0.5:
    print("Result: Pass")
else:
    print("Result: Fail")



# Import libraries
import tensorflow as tf
import numpy as np

# Sample dataset
X = np.array([[1], [2], [3], [4], [5]], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Create optimizer list
optimizers = {
    "SGD": tf.keras.optimizers.SGD(learning_rate=0.01),
    "Adam": tf.keras.optimizers.Adam(learning_rate=0.01),
    "RMSprop": tf.keras.optimizers.RMSprop(learning_rate=0.01)
}

# Train separate models
for name, opt in optimizers.items():

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),
        tf.keras.layers.Dense(1)
    ])

    model.compile(
        optimizer=opt,
        loss='mse'
    )

    model.fit(X, y, epochs=100, verbose=0)

    print(name, "Loss:",
          model.evaluate(X, y, verbose=0))
import numpy as np

image = np.array([
    [1, 2, 0, 3],
    [4, 5, 6, 1],
    [7, 8, 9, 2],
    [1, 2, 3, 4]
])

kernel = np.array([
    [1, 0],
    [0, -1]
])

output = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        region = image[i:i+2, j:j+2]
        output[i, j] = np.sum(region * kernel)

print(output)