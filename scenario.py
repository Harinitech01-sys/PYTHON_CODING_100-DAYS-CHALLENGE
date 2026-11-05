s= ['A', 'B', 'C', 'D'] 
k = 5
n=len(s)
k=k%n
result=s[k:]+s[:k]
print(result)


emails = ['a@x', 'b@x', 'a@x', 'c@x', 'b@x', 'a@x']

seen = set()
duplicates = []

for email in emails:
    if email in seen:
        if email not in duplicates:
            duplicates.append(email)
    else:
        seen.add(email)

first = duplicates[0] if duplicates else None

print("First:", first)
print("Duplicates:", duplicates)

votes = ['Ravi', 'Anu', 'Ravi', 'Anu', 'Meena', 'Ravi', 'Anu']

count = {}

for name in votes:
    count[name] = count.get(name, 0) + 1

for name, total in count.items():
    print(name, total)

winner = min(count, key=lambda name: (-count[name], name))

print("Winner:", winner)