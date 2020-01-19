```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x=abs(x)
        y=abs(y)
        
        if x==0 and y==0:
            return 0
               
        def bfs(i,j,x,y):
            
            queue=collections.deque([(i,j,0)])
            visited=set()
            visited.add((i,j))
        
            direct=[(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1)]
            
            while queue:
                curx,cury,step=queue.popleft()

                for i,j in direct:
                    next_x=curx+i
                    next_y=cury+j

                    if next_x>-4 and next_y>-4 and (next_x,next_y) not in visited:
                        if next_x==x and next_y==y:
                            return step+1
                        visited.add((next_x,next_y))
                        queue.append((next_x,next_y,step+1))
        return bfs(0,0,x,y)
```