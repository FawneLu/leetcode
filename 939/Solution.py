```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S=set(map(tuple,points))
        res=float('inf')
        for j,p2 in enumerate (points):
            for x in range(j):
                p1=points[x]
                if (p1[0]!=p2[0] and p1[1]!=p2[1] and (p1[0],p2[1]) in S and (p2[0],p1[1]) in S):
                    res=min(res,abs(p1[0]-p2[0])*abs(p1[1]-p2[1]))
        return res if res<float('inf') else 0

```

```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns=collections.defaultdict(list)
        for x,y in points:
            columns[x].append(y)
        lastx={}
        ans=float('inf')
        
        for x in sorted(columns):
            column=columns[x]
            column.sort()
            for j,y2 in enumerate(column):
                for i in range(j):
                    y1=column[i]
                    if (y1,y2) in lastx:
                        ans=min(ans,(x-lastx[y1,y2])*(y2-y1))
                    lastx[y1,y2]=x
        return ans if ans<float('inf') else 0
```