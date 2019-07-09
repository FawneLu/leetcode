- My Way  
In this way, we can find the index of the maximum number and then we sort the array. We judge from the second last number. If the number in the list isn't fit the situation then we break the loop and return -1.
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

- Second Way  
For this way, we can use two loops to find the largest number and the second largest number. We can judge whether the second largest one fit the situation. If so, the we return the index.
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