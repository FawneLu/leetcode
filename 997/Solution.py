```python
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            return N
        
        count=[0]*(N+1)
        for i,j in trust:
            count[i]-=1
            count[j]+=1
        
        for i in range(0,len(count)):
            if count[i]==N-1:
                return i
        
        return -1
```