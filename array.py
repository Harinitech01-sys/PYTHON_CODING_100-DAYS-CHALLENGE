#1) move zeros to the end
""""
arr=list(map(int,input().split()))
zeroes=[]
others=[]
for num in arr:
    if num==0:
        zeroes.append(num)
    else:
        others.append(num)
print(others+zeroes)



#2) Move negative numbers to the left
arr=list(map(int,input().split()))
negative=[]
positive=[]

for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print(negative+positive)

#3)  Move even numbers before odd numbers
arr=list(map(int,input().split()))
even=[]
odd=[]
for num in arr:
    if num % 2== 0:
        even.append(num)
    else:
        odd.append(num)
print(even+odd)

#4)Left rotate an array by one position

n = int(input())
arr = list(map(int, input().split()))

first = arr[0]

for i in range(n-1):
    arr[i] = arr[i+1]

arr[n-1] = first

print(*arr)


#5) 5: Left rotate an array by K positions
arr = list(map(int, input().split()))
k = int(input())

k = k % len(arr)
arr = arr[k:] + arr[:k]

print(*arr)


#6) Right rotate an array by K positions
arr = list(map(int, input().split()))
k = int(input())

k = k % len(arr)
arr = arr[-k:] + arr[:-k]

print(*arr)

#7)Reverse an array in groups of K
n = int(input())
a = list(map(int, input().split()))
k = int(input())

for i in range(0, n, k):
    left = i
    right = min(i + k - 1, n - 1)

    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

print(*a)

#8) Remove duplicates from a sorted array

arr=list(map(int,input().split()))
duplicates=[]
for num in arr:
    if num not in duplicates:
        duplicates.append(num)
print(duplicates)


#9) Merge two sorted arrays
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0
c = []

while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < n:
    c.append(a[i])
    i += 1

while j < m:
    c.append(b[j])
    j += 1

print(*c)

#10)missing number in an array
n = int(input())
a = list(map(int, input().split()))

total = n * (n + 1) // 2
missing = total - sum(a)

print(missing)
"""

#11,12 find duplicates in an array
n=int(input())
arr=list(map(int,input().split()))
result=[]
for i in arr:
    if i not in result:
        result.append(i)
    else:
        print(i)
        
n = int(input())
arr = list(map(int, input().split()))

result = []
duplicates = []

for i in arr:
    if i not in result:
        result.append(i)
    elif i not in duplicates:
        duplicates.append(i)

print(*duplicates)

#13. Find all elements that appear only once
n = int(input())
arr = list(map(int, input().split()))

result = []

for i in arr:
    if arr.count(i) == 1:
        result.append(i)

print(*result)

#14. Find the intersection of two arrays
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

result = []

for i in arr1:
    if i in arr2 and i not in result:
        result.append(i)

print(*result)

#15. Find the union of two arrays
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

result = []

for i in arr1 + arr2:
    if i not in result:
        result.append(i)

print(*result)