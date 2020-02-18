```python
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        for i in range(1,len(nums)):
            missing=nums[i]-nums[i-1]-1
            if  missing>=k:
                return nums[i-1]+k
            elif missing<k:
                k-=missing
        
        return nums[-1]+k
```