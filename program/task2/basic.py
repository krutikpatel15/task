# 1. List Comprehensions
x=int(input())
y=int(input())
z=int(input())
n=int(input())
i=[a for a in range(x+1)]
j=[b for b in range(y+1)]
k=[c for c in range(z+1)]
l=[[p,q,r] for p in i for q in j for r in k]
o=[]
for k in l:
    if sum(k) != n :
        o.append(k)
print(o)

# 2. Find the Runner-Up Score!
n=int(input())
a=list(map(int, input().split()))
b=max(a)
while b in a:
    a.remove(b)
print(max(a))

# 3. Nested Lists
n=int(input())
a=list()
b=list()
x=list()
y=list()
e=0
for i in range(n):
    a.append([])
    a[i].append(input())
    a[i].append(float(input()))
for i in range(n):
    b.append(a[i][1])
    y.append(a[i][1])
c=min(b)
while c in b:
    b.remove(c)
d=min(b)
for i in y:
    if d == i:
        x.append(a[e][0])
    e=e+1
x.sort()
for i in x:
    print(i)

# 4. Finding the percentage
n=int(input())
d=dict()
avg=0
for i in range(n):
    x=list(map(str,input().split()))
    d[x[0]]=[float(x[1]),float(x[2]),float(x[3])]
a=input()
if a in d:
    avg=sum(d[a])/3
print('%.2f'%avg)

# 5. Lists
a=0
l=list()
n=int(input())
for i in range(n):
    x=input()
    if x == "print":
        print(l)
    elif x == "sort":
        l.sort()
    elif x == "pop":
        l.pop()
    elif x == "reverse":
        l.reverse()
    elif "remove" in x:
        a = x.split(" ")
        l.remove(int(a[1]))
    elif "append" in x:
        a = x.split(" ")
        l.append(int(a[1]))
    elif "insert" in x:
        a = x.split(" ")
        l.insert(int(a[1]),int(a[2]))
        
# 6. Tuples
n=int(input())
t=list(map(int,input().split()))
x=tuple(t)
print(hash(x))

# 7. Introduction to Sets
def average(array):
    # your code goes here
    array = set(array)
    avg=sum(array)/len(array)
    return avg

#8. No Idea!
n,m=list(map(int,input().strip().split()))
x=list(map(int,input().strip().split()))
a=set(map(int,input().strip().split()))
b=set(map(int,input().strip().split()))
c=0
for i in x:
    if i in a:
        c=c+1
    elif i in b:
        c=c-1
print(c)

# 9. Symmetric Difference
m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
c=sorted((a.difference(b)).union(b.difference(a)))
for i in c:
    print(i)
    
# 10. Set .add()
x=set()
for i in range(int(input())):
    x.add(input())
print(len(x))

# 11. Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    x=list(input().split())
    if x[0]=='pop':
        s.pop()
    elif x[0]=='remove':
        s.remove(int(x[-1]))
    elif x[0]=='discard':
        s.discard(int(x[-1]))
print(sum(s))

# 12. Set .union() Operation
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
print(len(a|b))

# 13. Set .intersection() Operation
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
print(len(a&b))

# 14. Set .difference() Operation
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
print(len(a-b))

# 15. Set .symmetric_difference() Operation
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
print(len(a^b))

# 16. Set Mutations
a=int(input())
x=set(map(int,input().split()))
n=int(input())
for i in range(n):
    y=list(input().split())
    z=set(map(int,input().split()))
    if y[0]=='intersection_update':
        x&=z
    if y[0]=='update':
        x|=z
    if y[0]=='symmetric_difference_update':
        x^=z
    if y[0]=='difference_update':
        x-=z
print(sum(x))

# 17. The Captain's Room
from collections import Counter
n=int(input())
k=list(map(int,input().split()))
k=dict(Counter(k))
for key,value in k.items():
    if value!=n:
        print(key)
        break
        
# 18. Check Subset
t=int(input())
for i in range(t):
    a=int(input())
    x=set(map(int,input().split()))
    b=int(input())
    y=set(map(int,input().split()))
    if x==(x&y):
        print('True')
    else:
        print('False')
        
# 19. Check Strict Superset
a=set(map(int,input().split()))
n=int(input())
for i in range(n):
    x=set(map(int,input().split()))
    if (x&a==x) and (len(a)!=len(x)):
        c=1
    else:
        c=0
        break
print(bool(c))
