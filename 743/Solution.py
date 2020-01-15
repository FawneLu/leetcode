```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))
        
        dist={node: float('inf') for node in range(1,N+1)}
        
        def dfs(node,time):
            if time>=dist[node]:
                return 
            dist[node]=time
            for t, n in sorted(graph[node]):
                dfs(n,time+t)
                
        dfs(K,0)
        res=max(dist.values())
        return res if res<float('inf') else -1
```