- Use built-in function  
We can create a dictionary and use counter to count all the numbers in the list. If the value equals to 1, then we return the key.  
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

- Sort  
Firstly, we can sort the nums then we use range with the interval equals to 3.  
```python
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)-1,3):
            if nums[i]!=nums[i+1]:
                return nums[i]
            
        return nums[-1]
```
- Reference from Master Zhang  
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