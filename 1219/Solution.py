```python
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,grid,visited):
            res=0
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]==0:
                return -1
            visited.add((i,j))
            res=grid[i][j]+max(res,max(dfs(i+x,j+y,grid,visited) for (x,y) in [(0,1),(1,0),(-1,0),(0,-1)]))
            visited.remove((i,j))
            
            return res
        
        res=max(dfs(i,j,grid,set()) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]!=0)
        return res
```