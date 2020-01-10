```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sour=set(source)
        tar=set(target)
        for t in tar:
            if t not in sour:
                return -1
        
        res=0
        j=0
        while j<len(target):
            i=0
            while i<len(source) and j<len(target):
                if target[j]==source[i]:
                    i+=1
                    j+=1
                else:
                    i+=1
            res+=1
        
        return res
```