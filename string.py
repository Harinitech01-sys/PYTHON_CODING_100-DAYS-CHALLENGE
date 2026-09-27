#1)Character frequency
"""
word=input("Enter a word: ")
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
"""
#2) First Non-Repeating Character
"""
word = input()
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in word:
    if freq[ch] == 1:
        print(ch)
        break
"""

#3) Remove Duplicates
"""
word = input()
seen = set()
result = ""

for ch in word:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)

"""
#4) First Repeating Character
"""
word = input()
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in word:
    if freq[ch] >1:
        print(ch)
        break
"""

#Q5 — Palindrome using Two Pointers
"""
word = input()
left = 0
right = len(word) - 1

while left < right:
    if word[left] != word[right]:
        print("Not Palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome")
"""