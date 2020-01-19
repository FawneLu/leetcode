```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        
        def dfs(x,y):
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny]>matrix[x][y]:
                    if not dp[nx][ny]:
                        dp[nx][ny]=dfs(nx,ny)
                    dp[x][y]=max(dp[x][y],dp[nx][ny]+1)
            dp[x][y]=max(dp[x][y],1)
            return dp[x][y]
        
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j]=dfs(i,j)
        
        
        return max([max(x) for x in dp])
```