- Silly Way  
We use the built-in function counter to count the appearnce of each number then store the result in the dictionary.  
```python
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        temp_dict=Counter(nums)
        for key,value in temp_dict.items():
            if value >n/2:
                return key
```  
- We can sort the list and return the one on the n/2 position because this will secure this number appears more than n/2.
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
```