```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        if n==0:
            return 0
        
        res=0
        dp=[[0]*n for i in range(m)]
        
        for i in range(m):
            if matrix[i][0]=='1':
                dp[i][0]=1
                res=1
        
        for j in range(n):
            if matrix[0][j]=='1':
                dp[0][j]=1
                res=1
            
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
                
                res=max(res,dp[i][j])
                
        print(dp)
        
        return res*res
```