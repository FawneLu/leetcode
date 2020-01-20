```python
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        for x, w in enumerate(wells):
            pipes.append((x+1,0,w))
        pipes.sort(key=lambda x:x[-1])
        
        graph={i:i for i in range (n+1)}
        rank=[1]*(n+1)
        
        
        def find(i):
            while i!=graph[i]:
                i=graph[i]
            return i
        
        res=0
        count=0
        
        for x,y,w in (pipes):
            x=find(x)
            y=find(y)
            if x!=y:
                graph[x]=y
                res+=w
                count+=1
                if count==n:
                    return res
        
        return res
```