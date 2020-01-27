```python
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sticks=sorted(sticks)
        res=0
        while len(sticks)>1:
            s1=heapq.heappop(sticks)
            s2=heapq.heappop(sticks)
            res=res+s1+s2
            heapq.heappush(sticks,s1+s2)
        return res
```