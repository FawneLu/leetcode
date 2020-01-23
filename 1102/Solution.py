```python
from heapq import *
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        
        if not A or not A[0]:
            return 0
        
        m, n = len(A), len(A[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        queue = [[-A[0][0], 0, 0]] 
        visited = set([0,0])
        heapify(queue)

        while queue:
            print(queue)
            score, x0, y0 = heappop(queue) 
            if [x0, y0] == [m - 1, n - 1]: 
                return -score 
            
            for k in range(4): 
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heappush(queue, [max(score, -A[x][y]), x, y])
```