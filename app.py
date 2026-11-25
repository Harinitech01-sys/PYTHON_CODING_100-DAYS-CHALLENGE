
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
import random


def generate_lucky_numbers(count=5, max_num=50):
    """Generates a sorted list of unique random numbers."""
    numbers = random.sample(range(1, max_num + 1), count)
    return sorted(numbers)


def main():
    print("Welcome to the Lucky Number Generator!")
    user_name = input("Enter your name: ").strip() or "Friend"

    lucky_numbers = generate_lucky_numbers()
    print(f"\nHello, {user_name}! Your lucky numbers today are:")
    print(", ".join(map(str, lucky_numbers)))


if __name__ == "__main__":
    main()

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter subject {i+1} mark: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
    
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition:")
print(A + B)

print("\nMultiplication:")
print(A * B)

print("\nMatrix Multiplication:")
print(np.dot(A, B))

print("\nTranspose:")
print(A.T)

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Training data
X = np.array([[0], [1], [2], [3], [4]])
y = np.array([[0], [2], [4], [6], [8]])

# Create model
model = Sequential([
    Dense(8, activation='relu', input_shape=(1,)),
    Dense(1)
])

# Compile model
model.compile(
    optimizer='adam',
    loss='mse'
)

# Train model
model.fit(X, y, epochs=100, verbose=0)

# Prediction
result = model.predict(np.array([[5]]), verbose=0)

print("Prediction for 5:", result)
balance = 5000

while True:
    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully!")
        else:
            print("Enter a valid amount")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")
        
        
    books = []

def add_book():
    name = input("Enter book name: ")
    books.append(name)
    print("Book added successfully!")

def view_books():
    print("\nAvailable Books:")

    if len(books) == 0:
        print("No books available")
    else:
        for book in books:
            print("-", book)

def search_book():
    name = input("Enter book to search: ")

    if name in books:
        print("Book found!")
    else:
        print("Book not found!")

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice")from sklearn.linear_model import LinearRegression

x = [[1], [2], [3], [4]]
y = [10, 20, 30, 40]

model = LinearRegression()
model.fit(x, y)

print(model.predict([[5]]))
from sklearn.linear_model import LogisticRegression

x = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = LogisticRegression()
model.fit(x, y)

print(model.predict([[3]]))

from sklearn.neighbors import KNeighborsClassifier

x = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=1)
model.fit(x, y)

print(model.predict([[3]]))

from sklearn.tree import DecisionTreeClassifier

x = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(x, y)

print(model.predict([[4]]))

from sklearn.tree import DecisionTreeClassifier

x = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(x, y)

print(model.predict([[4]]))import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Study_Hours': [1, 2, 3, 4, 5],
    'Attendance': [60, 65, 70, 80, 90],
    'Marks': [40, 50, 60, 75, 90]
}

df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()

