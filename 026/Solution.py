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
def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return 1
        
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow-1]:
                continue
            nums[slow] = nums[fast]
            slow += 1
        return slow