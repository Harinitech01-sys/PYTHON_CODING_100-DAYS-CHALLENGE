

# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print(result)


# s = input()

# freq = {}

# # Count frequency
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# # Find first non-repeating character
# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break
# else:
#     print("No non-repeating character")


# s = input()
# words = s.split()

# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)


# s=input()
# result=""
# count=1

# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         count+=1
#     else:
#         result+=s[i-1]+str(count)
#         count=1
# result+=s[-1]+str(count)
# print(result)

# s=input()
# vowels={'a','e','i','o','u'}
# result=[]
# for ch in s:
#     if ch in vowels:
#         result.append("V")
#     else:
#         result.append("C")
# print(print("".join(result)))
        
        
# s1 = input()
# s2 = input()

# if len(s1) == len(s2) and s2 in s1 + s1:
#     print("Rotation")
# else:
#     print("Not Rotation")