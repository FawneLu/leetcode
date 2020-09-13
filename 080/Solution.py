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


    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 2:
            return 2
        
        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] == nums[slow - 2]:
                continue
            nums[slow] = nums[fast]
            slow += 1
        return slow