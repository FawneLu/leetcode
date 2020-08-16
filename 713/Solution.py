class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        res = 0
        tmp_p = 1
        i = 0
        
        for j in range(len(nums)):
            tmp_p *= nums[j]
            while tmp_p >= k:
                tmp_p /= nums[i]
                i += 1
            
            res += j-i+1
        return res