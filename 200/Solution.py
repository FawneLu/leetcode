```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    grid[i][j]=='0'
                    self.dfs(grid,i,j)
                    res+=1
        return res
    
    def dfs(self,grid,i,j):
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            dx=direction[0]+i
            dy=direction[1]+j
            if dx>=0 and dy>=0 and dx<len(grid) and dy<len(grid[0]):
                if grid[dx][dy]=='1':
                    grid[dx][dy]='0'
                    self.dfs(grid,dx,dy)
```