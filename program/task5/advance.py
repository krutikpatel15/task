# 1. Subsets
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst=[[]]
        for i in range(1,len(nums)+1):
            for i in list(combinations(nums,i)):
                lst.append(list(i))
        return(lst)
      
      
# 2. Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=0
        d=bin(x^y).replace("0b","")
        lst=[]
        lst[:0]=d
        for i in range(len(lst)):
            if lst[i] == '1':
                c+=1
        return(c)
      
      
# 3. Single Number II
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        for key,value in c.items():
            if value==1:
                return(key)
