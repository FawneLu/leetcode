- Just One Way Firstly  
Firstly, we use index to record the position of the number we need to judge, and a point to record the number which is not replicated. If the number in the list is not equal to the point, then index plus one, and make the prev equal to the number.  
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        prev = None
        for num in nums:
            if num != prev:
                nums[index] = num
                index += 1
                prev = num
        return index
```