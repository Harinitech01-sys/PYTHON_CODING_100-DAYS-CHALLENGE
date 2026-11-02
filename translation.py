
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load public AI model
model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Function to get AI response
def ask_ai(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=60)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# 1. Zero-shot prompting
print("\n1. ZERO SHOT")
print(ask_ai("What is Artificial Intelligence?"))

# 2. Few-shot prompting
print("\n2. FEW SHOT")
print(ask_ai("""
Translate into French:
Hello = Bonjour
Thank you = Merci
Good morning =
"""))

# 3. Role-playing prompting
print("\n3. ROLE PLAYING")
print(ask_ai("Act as a teacher and explain Python."))

# 4. Persona-based prompting
print("\n4. PERSONA BASED")
print(ask_ai("You are a friendly teacher. Explain AI simply."))

# 5. Reasoning prompting
print("\n5. REASONING")
print(ask_ai("What is 10 + 20? Explain briefly."))

print("\nExperiment completed successfully!")
