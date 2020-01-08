```python
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        W = sorted([w.count(min(w)) for w in words])
         
        res=[]
        for i in queries:
            cnt=0
            count=i.count(min(i))
            for j in W:
                if count<j:                        
                    cnt+=1
            res.append(cnt)
        return res
```