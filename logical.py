""""
a = [4, 8, 15, 16]
total = 0
for i in range(1, len(a), 2):
 total += a[i]
print(total) 

a = [3, 1, 4, 1, 5]
mx = a[0]
for i in range(1, len(a)):
 if a[i] > mx:
  mx = a[i]
print(mx)


a = [1, 2, 3, 4]
total = 0
for x in a:
 total += x
print(total // len(a))
print(total / len(a))


a = [0] * 5
a[2] = 7
a[4] = a[2] + 1
print(a)
Q1. Compute the sum and average of a list of n integers.
Q2. Find the maximum element and the index where it first occurs.
Q3. Reverse a list in place.
Q4. Count how many elements are even.
Q5. Return true if the list is sorted in ascending order (equal neighbours allowed), else false.
Mention the edge cases.

"""

arr=list(map(int,input().split()))
"""
total=0
for i in range(len(arr)):
    total+=arr[i]
print(total)
print(total / len(arr))

""""""

maximum = arr[0]
max_index = 0

for i, num in enumerate(arr):
    if num > maximum:
        maximum = num
        max_index = i

print("Maximum:", maximum)
print("Index:", max_index)"""
for i in range(len(arr) // 2):
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
print(arr)