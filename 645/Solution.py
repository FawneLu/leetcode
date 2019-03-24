```python
from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        rep_num = None
        tmp_dict = Counter(nums)
        for key, value in tmp_dict.items():
            if value == 2:
                rep_num = key
        
        return [rep_num, sum(range(1,len(nums)+1)) - (sum(nums) - rep_num)]
```  
```python
class Solution(object):
    def findErrorNums(self, nums):
        res = []
        for index in nums:
            if nums[abs(index)-1]<0:
                res.append(abs(index))
            else:
                nums[abs(index)-1]*=-1
        
        for i,num in enumerate(nums):
            if num>0:
                res.append(i+1)
        
        return res
``` 