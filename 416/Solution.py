```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp=[[0]*(sum(nums)+1) for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=1
        for j in range(1,target+1):
            dp[0][j]=0
        
        
        dp[0][0]=1
        
        for i in range(1,len(nums)+1):
            for j in range(0,target+1):
                if j >=nums[i-1]:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[len(nums)][target]
```