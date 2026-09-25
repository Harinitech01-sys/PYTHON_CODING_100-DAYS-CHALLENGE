"""CASE STUDY 1 — 🏦 Bank Transaction Analyzer
Given a list of bank transactions containing:
(Account ID, Transaction Type, Amount)

1. Calculate the final balance for each account.
2. Find the account with the highest balance.
3. Find accounts whose balance is below ₹3000.
4. Count deposits and withdrawals for each account.
5. Display a complete summary for each account."""


"""transactions = [
    ("A101", "deposit", 5000),
    ("A102", "withdraw", 2000),
    ("A101", "withdraw", 1000),
    ("A103", "deposit", 7000),
    ("A102", "deposit", 3000),
    ("A101", "deposit", 2000),
    ("A103", "withdraw", 2500),
    ("A104", "deposit", 4500),
    ("A102", "withdraw", 1000),
    ("A104", "withdraw", 1500),
    ("A101", "withdraw", 500),
    ("A103", "deposit", 1500),
    ("A105", "deposit", 2500),
    ("A105", "withdraw", 500),
    ("A102", "deposit", 2000)
]

balance = {}
deposits = {}
withdrawals = {}

for account, transaction_type, amount in transactions:

    if account not in balance:
        balance[account] = 0
        deposits[account] = 0
        withdrawals[account] = 0

    if transaction_type == "deposit":
        balance[account] += amount
        deposits[account] += 1

    elif transaction_type == "withdraw":
        balance[account] -= amount
        withdrawals[account] += 1

print("Final Balance:")
for account, amount in balance.items():
    print(account, ":", amount)

highest_account = max(balance, key=balance.get)

print("\nHighest Balance:")
print(highest_account, ":", balance[highest_account])

print("\nAccounts Below 3000:")
for account, amount in balance.items():
    if amount < 3000:
        print(account, ":", amount)

print("\nTransaction Count:")
for account in balance:
    print(
        account,
        "Deposits:", deposits[account],
        "Withdrawals:", withdrawals[account]
    )

print("\nComplete Summary:")
for account in balance:
    print(
        account,
        "| Balance:", balance[account],
        "| Deposits:", deposits[account],
        "| Withdrawals:", withdrawals[account]
    )"""

""" Employee Salary Analyzer

Given the following dataset:

employees = [
    ("E101", "Arun", 25000),
    ("E102", "Priya", 32000),
    ("E103", "Rahul", 28000),
    ("E104", "Divya", 40000),
    ("E105", "Kiran", 30000)
]

Write a Python program to:

Find the highest salary.
Find the employee with the highest salary.
Find the average salary.
Display employees earning more than ₹30,000.

Concepts: for loop, tuples, conditions, max(), sum()."""



employees = [
    ("E101", "Arun", 25000),
    ("E102", "Priya", 32000),
    ("E103", "Rahul", 28000),
    ("E104", "Divya", 40000),
    ("E105", "Kiran", 30000)
]
maximum=0
for employee in employees:
    if employee[2]>maximum:
        maximum=employee[2]
        name=employee[1]

print("Highest Salary:", maximum)
print("Employee with Highest Salary:", name)
total=0
for employee in employees:
    total+=employee[2]
print("Average Salary:", total/len(employees))

for employee in employees:
    if employee[2]>30000:
        print(employee[1], "earns more than ₹30,000")
