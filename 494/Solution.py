```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n=len(nums)
        dp=[collections.defaultdict(int) for i in range(n+1)]
        dp[0][0]=1
        for i in range(n):
            for cur_sum,cnt in dp[i].items():
                dp[i+1][cur_sum+nums[i]]+=cnt
                dp[i+1][cur_sum-nums[i]]+=cnt
        
        return dp[n][S]
```