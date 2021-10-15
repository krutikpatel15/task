# 1. Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = list(map(str, address.split('.')))
        for i in range(1,2*(len(address)-1),2):
            address.insert(i,'[.]')
        x=str()
        for i in address:
            x+=i
        return(x)
      
# 2. Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if len(str(i))%2==0:
                c+=1
        return(c)
      
# 3. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i] == nums[j]) and (i<j):
                    c+=1
        return(c)
      
# 4. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=list()
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if (nums[j] < nums[i]) and (j!=i):
                    c+=1
            lst.append(c)
        return(lst)
      
# 5. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        x,y=int(n[0]),int(n[0])
        for i in range(1,len(n)):
            x*=int(n[i])
            y+=int(n[i])
        return(x-y)
      
# 6. XOR Operation in an Array
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x=start
        for i in range(start+2,2*n+start,2):
            x^=i
        return(x)
