class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j
        
    def removeDuplicates1(self, nums: List[int]) -> int:
        i, count = 0, 1
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
                
            i += 1
        
        return len(nums)