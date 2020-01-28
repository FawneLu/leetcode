```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank,cur,prev):
            low[cur]=rank
            res=[]
            for neighbour in edges[cur]:
                if neighbour==prev:
                    continue
                if not low[neighbour]:
                    res+=dfs(rank+1,neighbour,cur)
                low[cur]=min(low[cur],low[neighbour])
                if low[neighbour] >= rank + 1:
                    res.append([cur, neighbour])
            
            return res
        
        res=[]
        edges=collections.defaultdict(list)
        low=[0]*n
        for i,j in connections:
            edges[i].append(j)
            edges[j].append(i)
            
        
        
        return dfs(1, 0, -1)
```