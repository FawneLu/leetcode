```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums[0],nums[1])
        return max(self.robbery(nums[:len(nums)-1]),self.robbery(nums[1:len(nums)]))
    
    def robbery(self,nums):
        if not nums: return 0
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums[0],nums[1])
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
```