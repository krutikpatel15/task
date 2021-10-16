# 1. Polar Coordinates
import cmath
z=cmath.polar(complex(input()))
for i in z:
    print(i)
    
# 2. Find Angle MBC
import math
a=int(input())
b=int(input())
print(str(int(round(math.degrees(math.atan2(a,b)))))+chr(176))

# 3. Triangle Quest 2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i - 1)//9) * ((10**i - 1)//9))
    
# 4. Mod Divmod
a=int(input())
b=int(input())
print(a//b,a%b,divmod(a,b),sep='\n')

# 5. Power - Mod Power
a=int(input())
b=int(input())
c=int(input())
print(pow(a,b),pow(a,b,c),sep='\n')

# 6. Integers Come In All Sizes
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(a**b + c**d)

# 7. Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*(10**i - 1)//9)
