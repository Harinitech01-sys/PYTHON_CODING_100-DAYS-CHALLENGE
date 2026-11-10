from transformers import pipeline

# Text Generation
generator = pipeline("text-generation", model="distilgpt2")
print(generator("AI is", max_new_tokens=20))

# Text Classification
classifier = pipeline("sentiment-analysis")
print(classifier("I love artificial intelligence"))

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Data Collection and Preprocessing
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# 2. Model Selection and Building
model = Sequential([Dense(4, activation='relu', input_shape=(2,)),
                    Dense(1, activation='sigmoid')])

# 3. Model Compilation
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4. Model Training
model.fit(X, y, epochs=100, verbose=0)

# 5. Model Evaluation
print("Accuracy:", model.evaluate(X, y, verbose=0)[1])

# 6. Prediction
print("Prediction:", model.predict(X, verbose=0).round())