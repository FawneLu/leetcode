```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if m==0 or n==0:
            return 0
        shape=set()
    
        def dfs(x,y,pos,rela_pos):
            if grid[x][y]!=1:
                return
            grid[x][y]=0
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dire in directions:
                dx=x+dire[0]
                dy=y+dire[1]
                if dx>=0 and dx<m and dy>=0 and dy<n and grid[dx][dy]==1:
                    new_pos=(rela_pos[0]+dire[0],rela_pos[1]+dire[1])
                    pos.append(new_pos)
                    dfs(dx,dy,pos,new_pos)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    pos=[]
                    dfs(i,j,pos,(0,0))
                    shape.add(tuple(pos))
        
        print(shape)
        
        return len(shape)
```