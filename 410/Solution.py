```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        high=sum(nums)
        low=high//m
        while high>=low:
            n=m
            mid=low+(high-low)//2
            valid=True
            cursum=0
            
            for i in range(len(nums)):
                if nums[i]>mid:
                    valid=False
                    break
                if cursum+nums[i]>mid:
                    n-=1
                    cursum=0
                cursum+=nums[i]
                if n==0:
                    valid=False
                    break
            
            if valid:
                high=mid-1
            else:
                low=mid+1
        
        return low
```