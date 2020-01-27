```python
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n=len(stones)
        if (n-1)%(K-1)!=0:
            return -1
        
        sums_=[0]*(n+1)
        for i in range(n):
            sums_[i+1]=sums_[i]+stones[i]
            
        
        dp=[[0]*n for i in range(n)]
        
        
        for l in range(K,n+1):
            for i in range(n-l+1):
                j=i+l-1
                for m in range(i,j,K-1):
                    dp[i][j]=min(dp[i][m]+dp[m+1][j],dp[i][j])
                if (l-1)%(K-1)==0:
                    dp[i][j] += sums_[j + 1] - sums_[i]
           
        return dp[0][n - 1]
```