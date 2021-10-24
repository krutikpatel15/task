# 1. Arays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr=numpy.array(arr,float)
    arr=arr[::-1]
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# 2. Shape and Reshape
import numpy
arr = input().strip().split(' ')
arr=numpy.array(arr,int)
print(numpy.reshape(arr,(3,3)))


# 3. Transpose and Flatten
import numpy
n,m = map(int,input().split())
arr=numpy.array([input().strip().split(' ') for i in range(n)],int)
print(numpy.transpose(arr))
print(arr.flatten())


# 4. Concatenate
import numpy
n,m,p=map(int,input().split(' '))
arr1=numpy.array([input().split(' ') for i in range(n)], int)
arr2=numpy.array([input().split(' ') for i in range(m)], int)
print(numpy.concatenate((arr1,arr2),axis=0))


# 5. Zeros and Ones
import numpy
a=tuple(map(int, input().split(' ')))
print(numpy.zeros(a, dtype = numpy.int))
print(numpy.ones(a, dtype = numpy.int))


# 6. Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int, input().split(' '))
print(numpy.eye(n,m))


# 7. Array Mathematics
import numpy
n,m=map(int,input().split(' '))
a=numpy.array([input().split() for i in range(n)], int)
b=numpy.array([input().split() for i in range(n)], int)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a**b)


# 8. Floor, Ceil and Rint
import numpy
numpy.set_printoptions(sign=' ')
a=numpy.array(input().split(),float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# 9. Sum and Prod
import numpy
n,m=map(int,input().split())
arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.prod(numpy.sum(arr,axis=0),axis=0))


# 10. Min and Max
import numpy
n,m=map(int,input().split())
arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.max(numpy.min(arr, axis=1)))


# 11. Mean, Var, and Std
import numpy
n,m = map(int,input().split(' '))
arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.around(numpy.std(arr,axis=None),11))


# 12. Dot and Cross
import numpy
n=int(input())
arr1=numpy.array([input().split(' ') for i in range(n)],int)
arr2=numpy.array([input().split(' ') for i in range(n)],int)
print(numpy.dot(arr1,arr2))


# 13. Inner and Outer
import numpy
a=numpy.array(input().split(), int)
b=numpy.array(input().split(), int)
print(numpy.inner(a,b))
print(numpy.outer(a,b))


# 14. Polynomials
import numpy
arr=numpy.array(input().split(),float)
x=int(input())
print(numpy.polyval(arr,x))


# 15. Linear Algebra
import numpy
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for i in range(int(input()))])),2))
