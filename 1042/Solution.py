```python
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res=[0]*N
        graph=[[] for i in range(N)]
        for path in paths:
            graph[path[0]-1].append(path[1]-1)
            graph[path[1]-1].append(path[0]-1)
        
        for i in range(N):
            neighbor_colors=[]
            for j in graph[i]:
                neighbor_colors.append(res[j])
            for color in range(1,5):
                if color in neighbor_colors:
                    continue
                res[i]=color
                break
        return res
```