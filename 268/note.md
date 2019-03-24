- Sort  
We can sort the list first and return the number which is not equal to the index.  
```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
```
- Minus  
We can return the sum of non-missing list minus sum of the input list.  
```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1))-sum(nums)
```
- Bin Operation  
We can define x=0. Then we use ^. Since the index and the number need to equal to each other, so we can return x^index^nums[index].  
```python
def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(1,len(nums)+1):
            x = x^i^nums[i-1]
        return x
```  