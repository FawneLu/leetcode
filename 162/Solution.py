class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = left + (right-left) //2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left
        
        
        
    def findPeakElement1(self, nums: List[int]) -> int:
        
        i = 1
        
        while i<len(nums) and nums[i] > nums[i-1]:
            i += 1
    
        return i-1