```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph=collections.defaultdict(list)
        for i,x in enumerate(stones):
            for j in range(i):
                y=stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        N=len(stones)
        res=0
        visited=[False]*N
        
        for i in range(N):
            if not visited[i]:
                stack=[i]
                visited[i]=True
                while stack:
                    res+=1
                    node=stack.pop()
                    for n in graph[node]:
                        if not visited[n]:
                            stack.append(n)
                            visited[n]=True
                
                res-=1
        return res
```