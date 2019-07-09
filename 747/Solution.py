```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=nums.index(max(nums))
        nums.sort()
        i=len(nums)-2
        while i >=0:
            if nums[i]*2>nums[-1]:
                return -1
                break
            elif nums[i]*2<=nums[-1]:
                i-=1
        return index
``` 
```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        large,se_large=0,0
        pos=-1
        
        for index,num in enumerate(nums):
            if num>large:
                large=num
                pos=index
        
        for num in nums:
            if num!=large:
                se_large=max(num,se_large)
        
        if se_large*2<=large:
            return pos
        else:
            return -1
```