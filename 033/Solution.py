```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[high]:
                if nums[mid]<target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[mid]>target and target>=nums[low]:
                    high=mid-1
                else:
                    low=mid+1
        return -1
```