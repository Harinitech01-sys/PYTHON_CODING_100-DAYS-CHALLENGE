
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
