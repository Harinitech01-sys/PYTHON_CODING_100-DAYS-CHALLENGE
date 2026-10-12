#)LEAP YEAR
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))


#Sample Input 0
"""
3
Sample Output 0

123
"""


n = int(input())
for i in range(1, n + 1):
    print(i, end="")
    
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))