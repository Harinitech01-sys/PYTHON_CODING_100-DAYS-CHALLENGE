from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")
print(generator("AI is", max_new_tokens=20))
classifier = pipeline("sentiment-analysis")
print(classifier("I love artificial intelligence"))

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
def analyze_text():

    text = input("Enter a sentence: ")

    lower_text = text.lower()

    freq = {}
    for ch in lower_text:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    print("\n===== TEXT ANALYSIS =====")
    print("Total characters:", len(text))
    words = text.split()
    print("Total words:", len(words))
    vowels = 0
    consonants = 0

    for ch in lower_text:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Duplicate characters: ", end="")

    for ch, count in freq.items():
        if count > 1:
            print(ch, end=" ")
    print("\n\nCharacter Frequency:")

    for ch, count in freq.items():
        print(ch, ":", count)

    # Case conversion
    print("\nUppercase:", text.upper())
    print("Lowercase:", text.lower())
analyze_text()
