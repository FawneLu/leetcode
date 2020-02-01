```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        low,high=0,len(nums)-1
        i=self.binarySearch_first(nums,target,low,high)
        j=self.binarySearch_last(nums,target,low,high)
        return [i,j]
    
    def binarySearch_first(self,nums,key,low,high):
        if high < low:
            return -1
        mid = low+(high-low)//2

        if nums[mid] < key:
            return self.binarySearch_first(nums,key,mid+1,high )
        elif nums[mid] > key:
            return self.binarySearch_first(nums,key,low,mid-1)
        else:
            if mid == 0 or nums[mid-1] != key: 
                return mid
            else: 
                high = mid - 1
                return self.binarySearch_first(nums,key,low,mid-1)
    
    def binarySearch_last(self,nums,key,low,high):
        if high < low:
            return -1
        mid = low+(high-low)//2

        if nums[mid] < key:
            return self.binarySearch_last(nums,key,mid+1,high )
        elif nums[mid] > key:
            return self.binarySearch_last(nums,key,low,mid-1)
        else:
            if mid == len(nums)-1 or nums[mid+1] != key: 
                return mid
            else: 
                return self.binarySearch_last(nums,key,mid+1,high)
```