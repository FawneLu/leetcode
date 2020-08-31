class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0 , len(nums)-1
        if nums[right] > nums[left]:
            return nums[left]
        
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        
        return nums[left]