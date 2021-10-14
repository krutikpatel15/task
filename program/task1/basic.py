# 1. Say "Hello, World!" With Python
print("Hello, World!")

# 2. Python If-Else
n=int(input())
if n%2==0:
    if n>1 and n<6:
        print('Not Weird')
    elif n>5 and n<21:
        print('Weird')
    elif n>20:
        print('Not Weird')
elif n%2==1:
    print('Weird')

# 3. Arithmetic Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

# 4. Python: Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)

#5. Loops
n = int(input())
for i in range(n):
    print(i*i)
    
#6. Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here

    if year%100==0 and year%400==0:
        leap=True
    elif year%4==0 and year%100!=0:
        leap=True

    return leap

year = int(input())
print(is_leap(year))

# 7. Print Function
n = int(input())
for i in range(1,n+1):
    print(i,end='')
