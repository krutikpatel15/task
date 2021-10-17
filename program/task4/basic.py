# 1. sWAP cASE
def swap_case(s):
    return(s.swapcase())
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
# 2. String Split and Join
def split_and_join(a):
    a = a.split(" ")
    a = "-".join(a)
    return a
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# 3. What's Your Name?
def print_full_name(a, b):
    print("Hello",a,b+"! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
# 4. Mutations
def mutate_string(s, p, c):
    s = s[:p] + c + s[p+1:]
    return s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
# 5. Find a string
def count_substring(x, y):
    c=0
    z=x
    for i in range(0, len(x)-len(y)+1):
        if z[i:len(y)+i] == y:
            c=c+1
        z=x
    return c
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
    
# 6. String Validators
if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            break
    print(i.isalnum())
    for i in s:
        if i.isalpha():
            break
    print(i.isalpha())
    for i in s:
        if i.isdigit():
            break
    print(i.isdigit())
    for i in s:
        if i.islower():
            break
    print(i.islower())
    for i in s:
        if i.isupper():
            break
    print(i.isupper())
    
# 7. Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
# 8. Text Wrap
import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.fill(text=string)
    return(word_list)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
# 9. Designer Door Mat
x,y=list(map(int,input().split()))
for i in range(x//2):
    for j in range((x//2)*3-3*i):
        print('-',end="")
    for j in range(1+2*i):
        print('.|.',end="")
    for j in range((x//2)*3-3*i-1):
        print('-',end="")
    print('-')

for i in range((y-7)//2):
    print('-',end="")
print('WELCOME',end="")
for i in range((y-7)//2-1):
    print('-',end="")
print('-')

for i in range(x//2):
    for j in range(3*(i+1)):
        print('-',end="")
    for j in range((x-2)-2*i):
        print('.|.',end="")
    for j in range(3*i+2):
        print('-',end="")
    print('-')
    
# 10. String Formatting
def print_formatted(number):
    width = len("{0:b}".format(n))
    return [print(str(n).rjust(width), 
            oct(n)[2:].rjust(width), 
            hex(n)[2:].upper().rjust(width), 
            bin(n)[2:].rjust(width)
            ) for n in range(1, number+1)], 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
# 11. Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    # Alphabet Rangoli in Python - HackerRank Solution START
    width  = size*4-3
    string = ''

    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
        string = ''

    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
# 12. Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    x=s.split(' ')
    for i in range(len(x)):
        x[i]=x[i].capitalize()
    return(' '.join(x))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
# 13. The Minion Game
def minion_game(s):
    x,y=0,0
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            x+=len(s)-i
        else:
            y+=len(s)-i
    if(x>y):
        print('Kevin',x)
    elif(x==y):
        print('Draw')
    elif(x<y):
        print('Stuart',y)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
# 14. Merge the Tools!
from collections import OrderedDict
def merge_the_tools(s, k):
    x=list()
    z=s
    for i in range(len(s)//k):
        t=s[i*k:i*k+k]
        u=list(OrderedDict.fromkeys(t))
        x.append(''.join(map(str, u)))
        s=z
    for i in x:
        print(i)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
