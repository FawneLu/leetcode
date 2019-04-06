- Just One Way  
We need to run this code in-place. If the num in the nums equals to 0, then we make nums[index]=num. Index begins from 0 and everytime we find a not 0 element, we make index plus one. The we use 0 to fill the rest of the list.
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index=0
        for num in nums:
            if num!=0:
                nums[index]=num
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0
```