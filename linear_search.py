#linear search basic
"""patient_ids = [1023, 1045, 1089, 1012, 1067, 1102, 1034]
target=int(input("Enter the patient ID to search for: "))
found=False
for i in range(len(patient_ids)):
    if patient_ids[i]==target:
        found=True
        break

if found:
    print(f"Patient ID {target} found : ",i)
else:
    print(f"Patient ID {target} not found.")"""
"""
roll_numbers = [105, 112, 118, 125, 131, 145, 152]
target=int(input("Enter the roll number to search for: "))

found=False
for i in range(len(roll_numbers)):
    if roll_numbers[i]==target:
        found=True
        break
if found:
    print(f"Roll number {target} found at index: ",i)
else:
    print(f"Roll number {target} not found.")
"""
"""_summary_
   
product_codes = [101, 205, 101, 310, 205, 450, 101]

target = int(input())

found = False

for num in range(len(product_codes)):
    if product_codes[num] == target:
        found = True
        break

if found:
    print("First occurrence is at index:", num)
else:
    print("Product not found")"""
"""  
transactions = [101, 205, 101, 310, 205, 450, 101]

target = int(input())

last = -1

for i in range(len(transactions)):
    if transactions[i] == target:
        last = i

if last != -1:
    print("Last occurrence of", target, "is at index:", last)
else:
    print("Transaction not found")
    """
#count of the order
"""
book_ids = [101, 205, 101, 310, 205, 101, 450, 101]

target = int(input())

count = 0

for i in range(len(book_ids)):
    if book_ids[i] == target:
        count += 1

if count > 0:
    print(target, "was borrowed", count, "times")
else:
    print(target, "was borrowed 0 times")
"""

# find all occurences
"""
    scores = [4, 6, 1, 4, 2, 6, 4, 1, 4]

target = int(input())

indices = []

for i in range(len(scores)):
    if scores[i] == target:
        indices.append(i)

if len(indices) > 0:
    print("Score occurred at indices:", indices)
else:
    print("Score not found")
 """
# topic: linear search with condition
"""
transactions = [450, 1200, 750, 3000, 650, 1800, 250]

found = False

for i in range(len(transactions)):
    if transactions[i] > 1000:
        print("First transaction greater than 1000 is", transactions[i], "at index", i)
        found = True
        break

if not found:
    print("No transaction found")
 """  
 
#Username Checker
"""
usernames = ["harini", "arun", "priya", "kavin", "meena", "rahul"]

target = input("Enter username: ")

found = False

for i in range(len(usernames)):
    if usernames[i] == target:
        print("Username found at index:", i)
        found = True
        break

if not found:
    print("Username not found")
"""
#Classroom Seating: 2D Array Search
#Topic: Linear Search in a 2D Array
""""
seats = [
    [101, 102, 103, 104],
    [105, 106, 107, 108],
    [109, 110, 111, 112]
]

target = int(input("Enter roll number: "))

found = False

for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == target:
            print("Student found at row", i, "column", j)
            found = True
            break
    if found:
        break

if not found:
    print("Student not found")
    """