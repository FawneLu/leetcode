- Normal Way  
We can use a dictionary to count the number of appearance of the value in the list. If the value in the dictionary is 2, then we return the corresponding index.  Then we use the difference(差) to get the missing value.(应有的list减去（input-重复值）)  
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

- Position Reverse  
This is a tricky way. If the number in the list isn't replicated, then we make the number multiply -1. Before this, we need to judge whether the number is smaller than 0. If so, means the number has been existed. Then we get the replicated number.  
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