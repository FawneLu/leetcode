class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
                
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return False