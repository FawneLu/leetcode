class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for i in range (m)]
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for i in range(1,m):
            dp[i][0]= int(obstacleGrid[i][0] == 0 and dp[i-1][0] == 1)
        for j in range(1,n):
            dp[0][j]= int(obstacleGrid[0][j] == 0 and dp[0][j-1] == 1)
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0
    
        return dp[-1][-1]