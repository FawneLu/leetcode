class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        sum_val=0
        dp=[0]*3
        for i in range(n-1,-1,-1):
            sum_val+=stoneValue[i]
            dp[i%3]=sum_val-min(dp[(i+k)%3] for k in range(1,4))
        
        if dp[0]*2==sum_val:
            return "Tie"
        if dp[0]*2>sum_val:
            return "Alice"
        if dp[0]*2<sum_val:
            return "Bob"
        
        
    def stoneGameIII1(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        sum_val=0
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            sum_val+=stoneValue[i]
            dp[i]=sum_val-min(dp[i+k] for k in range(1,4) if i+k<=n)
        
        if dp[0]*2==sum_val:
            return "Tie"
        if dp[0]*2>sum_val:
            return "Alice"
        if dp[0]*2<sum_val:
            return "Bob"