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