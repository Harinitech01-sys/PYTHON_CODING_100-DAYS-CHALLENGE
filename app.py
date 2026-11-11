
print("Welcome to Python Quiz!")

score = 0

print("\nWhich keyword is used to define a function in Python?")
print("A) function")
print("B) def")
print("C) fun")
print("D) define")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score:", score)
# Word Embedding using Keras

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding

# Input token IDs
data = np.array([[1, 2, 3, 4]])

# Create embedding model
model = Sequential([
    Embedding(input_dim=10, output_dim=4, input_length=4)
])

# Generate embeddings
result = model.predict(data, verbose=0)

# Display output
print("Input Tokens:")
print(data)

print("Word Embeddings:")
print(result)
