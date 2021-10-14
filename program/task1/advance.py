# 1. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return(nums)
      
      
# 2. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=list()
        lst1=nums[0:n]
        lst2=nums[n:len(nums)]
        for i in range(n):
            lst.append(lst1[i])
            lst.append(lst2[i])
        return(lst)
      
      
# 3. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst=list()
        for i in candies:
            if (i+extraCandies) >= max(candies):
                lst.append(bool(1))
            else:
                lst.append(bool(0))
        return(lst)
