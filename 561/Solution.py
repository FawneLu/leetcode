```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=0
        for i in range(0,len(nums),2):
            count=count+nums[i]
        return count
```
