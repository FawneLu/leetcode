```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            
        if nums[0]>target:
            return 0
        if nums[-1]<target:
            return len(nums)
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return i+1
                
                
                
        def binarysearch(nums,key):
            low,high=0,len(nums)-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]==key:
                    return mid
                elif nums[mid]<key:
                    low=mid+1
                elif nums[mid]>key:
                    high=mid-1  
            return -1
        
        if nums[0]>target:
            return 0
        if nums[-1]<target:
            return len(nums)
        if target in nums:
            return binarysearch(nums,target)
        else:
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return i+1
```