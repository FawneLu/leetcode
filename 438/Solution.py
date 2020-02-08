```python
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        m=len(s)
        n=len(p)
        if m<n:
            return []
        
        s_count=Counter(s[:n-1])
        p_count=Counter(p)
        
        for i in range(n-1,m):
            s_count[s[i]]+=1
            if s_count==p_count:
                res.append(i-n+1)
            s_count[s[i-n+1]]-=1
            if s_count[s[i-n+1]]==0:
                del s_count[s[i-n+1]]
        
        return res
```