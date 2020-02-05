```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            res=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    res=max(res,dp[j]+1)
            
            dp[i]=res
        return max(dp)
```