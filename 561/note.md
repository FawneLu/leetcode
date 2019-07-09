- 捞捞的 Way 
In this way, we can see that wto make the sum to be as large as possible, what we need to do is to sort the array first and then plus the number with the interval 2.     
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
