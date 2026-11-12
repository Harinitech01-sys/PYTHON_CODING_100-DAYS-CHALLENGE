
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
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    note = input("Enter a short note: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, f"{amount:.2f}", note])
    print("Expense saved successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    total = 0.0
    print("\n--- Your Expenses ---")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row:
                print(f"{row[0]} | {row[1]} | ${row[2]} | {row[3]}")
                total += float(row[2])
    print(f"---------------------\nTotal Spent: ${total:.2f}\n")

def main():
    initialize_file()
    while True:
        print("1. Add Expense")
        print("2. View Expenses & Total")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

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
