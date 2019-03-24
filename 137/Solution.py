```python
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict=Counter(nums)
        for key, value in num_dict.items():
            if value==1:
                return key
```  
```python
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)-1,3):
            if nums[i]!=nums[i+1]:
                return nums[i]
            
        return nums[-1]
```
```python
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        a = 0; b = 0
        for i in range(len(nums)):
            b = b^nums[i] & ~a
            a = a^nums[i] & ~b

        return b
```