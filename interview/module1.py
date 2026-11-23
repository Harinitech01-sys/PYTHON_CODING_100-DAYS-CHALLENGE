# arr=list(map(int,input().split()))
# largest=float('-inf')
# second_largest=float('-inf')

# for i in arr:
#     if i>largest:
#         largest=i
#         second_largest=largest
#     else if  i> second_largest and i != largest:
#         second_largest=i
# print(largest)
# print(second_largest)


# left=0
# right=len(arr)-1

# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)


# arr = [10, 20, 30, 40, 50]
# result = []

# for i in range(len(arr)-1, -1, -1):
#     result.append(arr[i])

# print(result)

# arr = [1, 2, 2, 3, 4, 4, 5, 1]
# duplicates=[]

# for num in arr:
#     if num  not in duplicates:
#         duplicates.append(num)
# print(duplicates)



# arr = [1, 2, 4, 5, 6]

# n = len(arr) + 1

# expected_sum = n * (n + 1) // 2

# actual_sum = 0

# for i in range(len(arr)):
#     actual_sum += arr[i]

# missing = expected_sum - actual_sum

# print("Missing number:", missing)

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]

# result=[]
# for num in a:
#     if num in b and num not in result:
#         result.append(num)
# print(result)

# arr = [0, 1, 0, 3, 12]
# zeroes=[]
# result=[]
# for num in arr:
#     if num==0:
#         zeroes.append(num)
#     else:
#         result.append(num)
# print(result+zeroes)

# arr = [1, 2, 3, 4, 5]
# k = 2

# print(arr[-k:] + arr[:-k])


# arr = [1, 2, 2, 3, 1, 4, 2]
# freq={}
# for num in arr:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
# for num , count in freq.items():
#     print(f"{num}: {count}")

# arr = [1, 5, 3, 6, 4, 7]
# even_index = []
# odd_index = []
# for i in range(len(arr)):
#     if i % 2 == 0:
#         even_index.append(arr[i])
#     else:
#         odd_index.append(arr[i])
# print("Even index elements:", even_index)
# print("Odd index elements:", odd_index)

# arr=list(map(int,input().split()))

# even_index=[]
# odd_index=[]

# for i in range(len(arr)):
#     if i%2==0:
#         even_index.append(arr[i])
#     else:
#         odd_index.append(arr[i])
        
# print("odd index elements:",odd_index)
# left=0
# right=len(even_index)-1
# while left<right:
#     even_index[left],even_index[right]=even_index[right],even_index[left]
#     left+=1
#     right-=1
# print("even index elements:",even_index)


# result = []

# for i in range(len(even_index)):
#     result.append(even_index[i])
#     result.append(odd_index[i])

# print(result)


# arr=list(map(int,input().split()))
# result=[]
# pos_index=[]
# neg_index=[]

# for i in range(len(arr)):
#     if arr[i] >0:
#         pos_index.append(arr[i])
#     elif i<0:
#         neg_index.append(arr[i])
        
# i = 0

# while i < len(pos) and i < len(neg):
#     result.append(pos[i])
#     result.append(neg[i])
#     i += 1

# # Add remaining positive numbers
# while i < len(pos):
#     result.append(pos[i])
#     i += 1

# # Add remaining negative numbers
# while i < len(neg):
#     result.append(neg[i])
#     i += 1

# print(result)


arr=list(map(int,input().split()))
# leader=[]
# largest=float('-inf')

# for i in range(len(arr)-1,-1,-1):
#     if arr[i]>largest:
#         largest=arr[i]
#         leader.append(arr[i])
# leader.reverse()
# print(leader)

total_sum=sum(arr)
left_sum=0

for i in range(len(arr)):
    right_sum = total_sum - left_sum - arr[i]

    if left_sum == right_sum:
        print("Equilibrium index:", i)
        break
    
    
        left_sum += arr[i]
else:
    print("No equilibrium index found")
    
    
arr = [2, 7, 11, 15, 3, 6]
target = 9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j]) 
    
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

i = 0
j = 0
result = []

# Compare elements from both arrays
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

# Add remaining elements from a
while i < len(a):
    result.append(a[i])
    i += 1

# Add remaining elements from b
while j < len(b):
    result.append(b[j])
    j += 1

print(result)



arr = [2, 2, 1, 2, 3, 2, 2]

freq = {}

# Step 1: Count frequency
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Step 2: Find majority element
for num, count in freq.items():
    if count > len(arr) // 2:
        print("Majority element:", num)
        break
else:
    print("No majority element")
    
    
    
arr=[1,2,3,4]
result=[]

for i in range(len(arr)):
    product=1
    for j in range(len(arr)):
        if i!=j:
            product*=arr[j]
    result.append(product)
print(result)


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)