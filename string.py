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

#6)Find the Longest Word
sentence = input()
words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

#7) Anagram Check 
s = input()
t = input()

if sorted(s) == sorted(t):
    print("Anagram")
else:
    print("Not Anagram")

#8)Longest Substring Without Repeating Characters
s = input()

seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    current_len = right - left + 1
    max_len = max(max_len, current_len)

print(max_len)

#9) Count Vowels and Consonants
s = input()
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in s:
    if ch in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(vowel_count, consonant_count)

#10) Compress a String 
s = input()

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)