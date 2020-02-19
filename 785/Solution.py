```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[0]*len(graph)
        for i in range(len(graph)):
            if graph[i] and visited[i]==0:
                visited[i]=1
                queue=collections.deque()
                queue.append(i)
                while queue:
                    v=queue.popleft()
                    for j in graph[v]:
                        if visited[j]:
                            if visited[j]==visited[v]:
                                return False
                        else:
                            visited[j]=3-visited[v]
                            queue.append(j)
        
        return True
```