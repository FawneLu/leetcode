```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res=[]
        people.sort(key=lambda x:(-x[0],x[1]))
        for p in people:
            res.insert(p[1],p)
        return res
```