
import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Cathy", "David", "Eva"],
    "Age": [21, 24, 29, 35, 42],
    "City": ["Chennai", "Chennai", "Coimbatore", "Madurai", "Coimbatore"],
    "Salary": [30000, 35000, 42000, 50000, 55000]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# Create pseudonym mapping
name_mapping = {
    name: f"P{i+1:03d}"
    for i, name in enumerate(df["Name"])
}

# Replace original names with pseudonyms
df["Name"] = df["Name"].map(name_mapping)

print("\nPseudonymised Dataset")
print(df)

# Store mapping separately
print("\nSecret Mapping Table")
print(name_mapping)
# Secret Message Decoder

message = "I love Python"

secret = ""

for letter in message:
    secret += chr(ord(letter) + 3)

print("Original:", message)
print("Secret:", secret)
print("Decoded:", "".join(chr(ord(c) - 3) for c in secret))



import random

compliments = [
    "You are amazing! 🌟",
    "Keep shining! ✨",
    "Your ideas are powerful! 💡",
    "You are born to achieve great things! 🚀",
    "Never stop believing in yourself! ❤️"
]

print(random.choice(compliments))

import random

number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("🎉 You are a genius!")
else:
    print("Oops! The number was", number)
    
    
mood = input("How are you feeling today? ").lower()

if mood == "happy":
    print("😊 Keep shining!")
elif mood == "sad":
    print("💗 Better days are coming!")
elif mood == "angry":
    print("🌿 Take a deep breath!")
elif mood == "tired":
    print("😴 Time to recharge!")
else:
    print("✨ You're unique. Keep going!")