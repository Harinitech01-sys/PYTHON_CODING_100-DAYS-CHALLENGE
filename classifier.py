from transformers import pipeline

# Text Generation
generator = pipeline("text-generation", model="distilgpt2")
print(generator("AI is", max_new_tokens=20))

# Text Classification
classifier = pipeline("sentiment-analysis")
print(classifier("I love artificial intelligence"))