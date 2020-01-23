```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        fresh=0
        queue=collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        if fresh==0:
            return 0
        
        step=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            for i in range(len(queue)):
                x,y=queue.popleft()
                for dire in directions:
                    nx=x+dire[0]
                    ny=y+dire[1]
                    if nx>=0 and nx<m and ny>=0 and ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        queue.append((nx,ny))
                        fresh-=1
            
            step+=1
        
        if fresh!=0:
            return -1
        return step-1
```