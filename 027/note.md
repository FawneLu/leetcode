- For this problem, we can learn the way in the problem 26. We use index to racord the position which the value in the nums is not equal to the input.
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        for num in nums:
            if num!=val:
                nums[index]=num
                index+=1
        return index
```